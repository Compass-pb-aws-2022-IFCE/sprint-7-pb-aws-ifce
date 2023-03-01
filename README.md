# Avaliação Sprint 7 - Programa de Bolsas Compass UOL / AWS e IFCE

[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/LogoCompasso-positivo.png/440px-LogoCompasso-positivo.png)](https://compass.uol/pt/home/)

Avaliação da sétima sprint do Programa de Bolsas Compass UOL para Formação em Machine Learning para AWS.

***

## Sumário
* [Objetivo](#objetivo)
* [Ferramentas](#ferramentas)
* [Desenvolvimento](#desenvolvimento)
* [Estrutura de Intenções/Slots](#estruturas)
* [Deploy da aplicação no Slack](#aplicacao)
* [Impedimentos](#impedimentos)
* [Autores](#autores)
* [Agradecimentos](#agradecimentos)


***
## Objetivo

Criar um chatbot utilizando o `Amazon Lex`, conectá-lo a uma plataforma de menssagem, nesse caso o `Slack`, com funções semelhantes à de uma PokeDex, logo capaz de prover informações específicas sobre pokémons.

***

## Ferramentas

* [AWS](https://aws.amazon.com/pt/) Plataforma de computação em nuvem da Amazon.
* [Amazon Lex](https://aws.amazon.com/pt/lex/) Serviço para criar interfaces de conversação em qualquer aplicativo usando voz e texto.
* [Lambda](https://aws.amazon.com/lambda/) Serviço de computação *serverless* que permite a execução de código sem a preocupação de gerenciar servidores.
* [Slack Api](https://api.slack.com/) 

***

## Desenvolvimento
*  Foi utilizado os serviços de `Serverles` e `Lambda` com o objetivo de  criar funções para trabalhar com algumas intents específicas. Os arquivos correspondentes estão na pasta "./src"

* A seguir é exibido o corpo da função _principal_ da aplicação que é chamada pelo `Lex`, de modo que, a partir dessa função serão evocadas outras funções.

``` python
def lambda_handler(event, context):
    intentName = event['sessionState']['intent']['name']
    
    response = prepareResponse(event,"Desculpe, poderia reescrever sua frase")
        
    if intentName=='info':
        
        if event['sessionState']['intent']['slots']['pokemon'] != None:
            
            pokemon = event['sessionState']['intent']['slots']['pokemon']['value']['originalValue']
            atributo = event['sessionState']['intent']['slots']['atributos']['value']['interpretedValue']
            
            payload = {'pokemon': pokemon, 'atributo': str(atributo)}
            
            response = lambda_client.invoke(FunctionName='pokebot-dev-func-info-pokemon', Payload=json.dumps(payload))
            result = json.loads(response['Payload'].read().decode())
            
            if result['pokemon'] != 'error':
                attributes = {
                    'peso': f"O pokemon {result['pokemon'].capitalize()} tem o peso de {float(result['atributo'])/10} quilos.",
                    'altura': f"O pokemon {result['pokemon'].capitalize()} tem a altura de {float(result['atributo'])/10} metros.",
                    'vida': f"O pokemon {result['pokemon'].capitalize()} tem {result['atributo']} pontos de vida.",
                    'ataque': f"O pokemon {result['pokemon'].capitalize()} tem {result['atributo']} pontos de ataque.",
                    'defesa': f"O pokemon {result['pokemon'].capitalize()} tem {result['atributo']} pontos de defesa."
                }
                if atributo in attributes:
                    response = prepareResponse(event, attributes[atributo])
                else:
                    response = prepareResponse(event, "Atributo inválido. Tente novamente.")
            else:
                response = prepareResponse(event, "Esse pokemon não existe!")
        else:
             response = prepareResponse(event,"Desculpe, reescreva sua frase passando qual pokemon deseja saber o atributo: " + "Ex: qual o peso do Pikachu")
    elif intentName=='CuriosidadesIntent':
 
        response = lambda_client.invoke(FunctionName='pokebot-dev-func-curiosidades-pokemon', Payload=json.dumps(event))
        response = json.loads((response["Payload"].read().decode('utf-8'))) 
        print(response)
        mensagem = response["body"]
        response = prepareResponse(event,mensagem)
    return response

```

***


## Estrutura de Intenções/Slots <a id="estruturas"></a>

### Intents

1. *Sucesso:* 
 É apenas uma saudação específica.

2. *Saudação:*
 É acionada ao se receber uma entrada que seja uma saudação e retorna um cumprimento do PokeBot.

3. *Info:*
 É acionada ao pedir alguma informação específica sobre algum pokémon, e possui dois __slots__: o nome do pokémon e o atributo que se deseja obter informações. Essa intent aciona uma função lambda que faz um tratamento no nome de pokémon inserido, utilizando distância de Levenshtein para encontrar a melhor correspondência de nomes de pokémons. Em seguida, é feita uma consulta a PokeAPI para obter a informação requerida e esta, se encontrada, é retornada ao usuário. 

4. *Curiosidades:*
 É acionada quando se pede uma informação ou fato mais 'genérico', e pode ser de três tipos: lendas, curiosidades (fatos interessantes) e piadas. Também utiliza __slot__ para capturar o tipo de curiosidade e chama uma função lambda para obter a resposta.

5. *InfoSobreInfo:*
 É uma função auxiliar que mostra informações sobre como utilizar o recurso de informações e utiliza cards para isso.

6. *InfoSobreCuriosidades:*
 Semelhante à anterior, mas voltada a dar informações sobre como consultar o recurso de curiosidades.

7. *Despedida:*
 É acionada ao receber alguma entrada que seja uma despedida, e encerra o chat.

8. *Fallback:*
 É acionada quando algum erro ocorre e não se pode compreender qual era a intenção do usuário.


### Slots
1. *Pokemon:* É do tipo `AMAZON.LastName` e é utilizado para capturar o nome/espécie do pokémon.

2. *Atributos:* É do tipo criado `caracterítica` que é utilizado para capturar o tipo de atributo que faz referência à informação pedida pelo usuário. O tipo possui os valores padrão: peso, altura, ataque, vida, defesa e alguns sinônimos.  

3. *Tipo:* É do tipo criado `Type` que é utilizado para especificar a curiosidade requerida pelo usuário. Este tipo tem valores os padrão: curiosidade, piada, lenda e sinônimos.



### Fluxogramas

#### Info Intent
![Info Intent - PokeBot](https://uploaddeimagens.com.br/images/004/372/814/original/InfoIntent.png?1677694081)

#### Curiosidades Intent
![Curiosidades Intent - PokeBot](https://uploaddeimagens.com.br/images/004/372/807/original/CuriosidadesIntent-PokeBot.png?1677693982)


***

## Deploy do Amazon Lex Bot no Slack <a id="aplicacao"/>

### Passo 1

Criar uma conta no [Slack](https://slack.com/). Logo após criar um Workspace.

### Passo 2 - Criar uma aplicação Slack

1. Fazer login no console da API do Slack em http://api.slack.com.
2. Criar uma aplicação (`Create an app`).
3. Configurar os recursos da aplicação: no menu esquerdo escolher `Interactivity & Shortcuts` e clicar no botão pra ativar. No campo `Request URL` especificar qualquer URL válida (esta será atualizada posteriormente) e então salvar as mudanças.
4. No menu esquerdo escolher `Basic Information`, obtendo assim as credenciais do aplicativo que serão utilizadas no _Amazon Lex_.

### Passo 3 - Integrar a aplicação Slack com o Amazon Lex Bot

1. Abrir console do Amazon Lex.
2. Selecionar o bot criado e escolher a guia `Canais`, adicione um canal.
3. Selecione a plataforma Slack, e escolha um nome para a integração.
4. Escolha o `Alias` do bot.
5. Digite a ID do cliente, o segredo do cliente e o token de verificação (Credenciais obtidas no passo anterior).
6. Por último clique em _Adicionar_, então será retornado duas URLs (`Endpoint`, `Endpoint OAuth`).

### Passo 4 - Completar a integração do Slack

1. Faça login novamente no console da API do Slack e selecione o aplicativo criado no passo 2.
2. Atualize o recurso `OAuth & Permissions`: na seção _Redirect URLs_ adicione a URL do OAuth fornecida pelo Amazon Lex e salve.
3. Na seção `Bot Token Scopes` adicione as duas permissões: `chat:write` e `team:read`.
4. Atualize o menu `Interactivity & Shortcuts`, no campo `Request URL` adicione a URL `Endpoint`, fornecida pelo Amazon Lex e salve.
5. No menu `Event Subscriptions`, ative a funcionalidade, e adicione a mesma URL do ponto 4. Na seção `Subscribe to bot events` adicione o evento `message.im`, para habilitar mensagens diretas entre o usuário final e o bot do Slack, então salve.
6. Por último vá no menu `App Home` e marque o checkbox da seção `Messages Tab`.

### Passo 5 - Testar a integração

1. No menu `Manage Distribution` escolha `Add to Slack` para instalar a aplicação e forneça as permissões.
2. Acesse seu Workspace do Slack, no menu esquerdo, na seção Apps, você notará que sua aplicação já está disponível, agora é só iniciar um bate-papo.
* Link para a aplicação:
    * [Aplicação - Slack](https://join.slack.com/t/sprint7-grupo2/shared_invite/zt-1q61sas4i-pE8_IqdsRleRmIQVrSn_8Q)


***

## Impedimentos
* Inicialmente houve algumas dificuldades em relação à integrar a função lambda ao bot.

* Problemas com a organização do fluxo de conversa de algumas intents.

* Dificuldade inicial de compartilhar o bot.

***

## Autores

* [@Herisson Hyan](https://github.com/herissonhyan)
* [@Rosemelry](https://github.com/Rosemelry)
* [@JosianaSilva](https://github.com/JosianaSilva)
* [@Edivalco Araujo](https://github.com/EdivalcoAraujo)


***
## Agradecimentos

Agradecemos pela documentação disponibilizada a qual foi muito útil no processo de criação do bot. :D

***
***