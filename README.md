# Avaliação Sprint 7 - Programa de Bolsas Compass UOL / AWS e IFCE

[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/LogoCompasso-positivo.png/440px-LogoCompasso-positivo.png)](https://compass.uol/pt/home/)

Avaliação da sétima sprint do Programa de Bolsas Compass UOL para formação em machine learning para AWS.

***

## Sumário
* [Objetivo](#objetivo)
* [Ferramentas](#ferramentas)
* [Desenvolvimento](#desenvolvimento)
* [Autores](#autores)

## Objetivo

Criar um chatbot utilizando o Amazon Lex, conectá-lo a uma plataforma de menssagem, nesse caso o Slack, com funções semelhantes à de uma PokeDex, logo capaz de prover informações específicas sobre pokémons.

***

## Ferramentas

* [AWS](https://aws.amazon.com/pt/) Plataforma de computação em nuvem da Amazon.
* [Amazon Lex](https://aws.amazon.com/pt/lex/) Serviço para criar interfaces de conversação em qualquer aplicativo usando voz e texto.
* [Lambda](https://aws.amazon.com/lambda/) Serviço de computação *serverless* que permite a execução de código sem a preocupação de gerenciar servidores.
* [Slack Api](https://api.slack.com/)

***

## Desenvolvimento

* Função chamada pelo *Lex* onde, a partir dessa função serão evocadas outras funções para trabalhar com as intents.

```
def lambda_handler(event, context):
    intentName = event['sessionState']['intent']['name']
    response = prepareResponse(event,"Desculpe, poderia reescrever sua frase")
    if intentName=='play':
        response = prepareResponse(event,"Função em desenvolvimento")
        
    elif intentName=='info':
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

## Estrutura e Lógica do Negócio

A aplicação possui vários recursos de uma pokédex, logo é possível obter informações, curiosidades a respeito de pokémons.

## Estrutura de Intenções/Slots

1. *Sucesso:* 
 É apenas uma saudação específica.

2. *Saudação:*
 É acionada ao se receber uma entrada que seja uma saudação e retorna um cumprimento do PokeBot.

3. *Info:*
 É acionada ao pedir alguma informação específica sobre algum pokémon, e possui dois slots: o nome do pokémon e o atributo que se deseja obter informações. Essa intent aciona uma função lambda que faz um tratamento no nome de pokémon inserido, utilizando distância de Levenshtein para encontrar a melhor correspondência de nomes de pokémons. Em seguida, é feita uma consulta a PokeAPI para obter a informação requerida e esta, se encontrada, é retornada ao usuário. 

4. *Curiosidades:*
 É acionada quando se pede uma informação ou fato mais 'genérico', e pode ser de três tipos: lendas, curiosidades (fatos interessantes) e piadas. Também utiliza slot para capturar o tipo de curiosidade e chama uma função lambda para obter a resposta.

5. *InfoSobreInfo:*
 É uma função auxiliar que mostra informações sobre como utilizar o recurso de informações e utiliza cards para isso.

6. *InfoSobreCuriosidades:*
 Semelhante à anterior, mas voltada a dar informações sobre como consultar o recurso de curiosidades.

7. *Despedida:*
 É acionada ao receber alguma entrada que seja uma despedida, e encerra o chat.

8. *Fallback:*
 É acionada quando algum erro ocorre e não se pode compreender qual era a intenção do usuário.

## Autores

* [@Herisson Hyan](https://github.com/herissonhyan)
* [@Rosemelry](https://github.com/Rosemelry)
* [@JosianaSilva](https://github.com/JosianaSilva)
* [@Edivalco Araujo](https://github.com/EdivalcoAraujo)
