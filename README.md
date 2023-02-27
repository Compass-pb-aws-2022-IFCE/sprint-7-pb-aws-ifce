# Avaliação Sprint 7 - Programa de Bolsas Compass UOL / AWS e IFCE


Avaliação da sétima sprint do programa de bolsas Compass UOL para formação em machine learning para AWS.


***

## Sumário

* [Objetivo](#objetivo)
* [Tecnologias](#tecnologias)
* [PetBot](#petbot)
  * [Intents](#intents)
  * [Slots](#slots)  
* [Desenvolvimento](#desenvolvimento)
* [Integração com Slack](#integrando-ao-slack)
* [Acesso ao Chatbot](#acesso-à-aplicação)  
* [Dificuldades](#dificuldades)
* [Conclusão](#conclusão)
* [Autores](#autores)

***
## Objetivo

Desenvolvimento de um chatbot utilizando a ferramenta Amazon Lex V2 e integração com uma API de mensagens a escolha do grupo de desenvolvedores.

*** 
## Tecnologias

* [Amazon Lex](https://aws.amazon.com/pt/lex/) 
* [Slack API](https://api.slack.com/)
*** 
## PetBot
![logo petbot](https://user-images.githubusercontent.com/80013300/221453200-dc3334e3-3292-4e48-bf62-2f7ce931ca35.png)

O PetBot é um chatbot desenvolvido na plataforma Amazon Lex V2 que visa auxiliar os donos de animais de estimação a cuidar de seus pets de forma prática, por meio dele o cliente pode comprar produtos para animais, receber dicas e cuidades e ainda agendar serviços oferecidos pelo petshop. 
Ele oferece uma interface conversacional simples e intuitiva, permitindo que os usuários interajam com o chatbot de forma natural e eficiente.


### Intents

* **SaudacaoIntent**:
Cumprimenta o usuário na inicialização do atendimento e pergunta sua intenção para direcioná-lo ao intent referente a ela.

* **AgendarServicoIntent**: Caso o cliente escolha essa opção no menu inicial, serão mostradas os tipos de serviços disponíveis e ele deve optar entre um deles (banho, tosa ou veterinário) ou retornar. A resposta será coletada em forma de slot e tratada em uma conditional branch para direcioná-lo a elicitação de slot mais espécifica para sua solicitação, cofirmando o agendamento no final.

* **AdquirirProdutoIntent**: É mais uma opção do menu incial, porém, neste caso serão mostradas as categorias de produto, sendo elas: ração, medicamento ou brinquedo. Ao escolher uma delas, o slot referente será preenchido e servirá de parâmetro para uma conditional branch que invocará o intent mais específico para a categoria selecionada.

* **ComprarBrinquedoIntent**:
Essa intent será invocada quando o usuário selecionar a categoria brinquedo. Nela serão mostradas as opções de brinquedo e a opção de sair caso o usuário não encontre o que busca. No final da compra será perguntado qual o próximo objetivo do cliente para que ele possa ser redirecionado mais rapidamente a ela.

* **ComprarRemedioIntent**: Essa intent funciona da mesma forma que a anterior, tanto o modo de invocação quanto a lógica. A diferença está apenas na listagem dos produtos, que agora são remédios, e nas informações solicitadas para sua realização. A separação se dá apenas por fins de setorização dos produtos.

* **ComprarRacaoIntent**: É mais uma intent que segue a mesma estrutura das duas anteriores, porém com os produtos sendo rações. Vale mencionar também que em todas intents desse tipo é solicitada confirmação para dar possibilidade de cancelar o procedimento.

* **DicasDeCuidadoIntent**: Nessa intent é perguntada a espécie do animal do cliente e partir dela são retornadas variadas dicas de cuidado.

* **EncerramentoIntent**: Essa intent é opção em todas etapas do atendimento, serve para o encerrar o atendimento no momento em que desejar.

* **FallbackIntent**: Intent padrão que serve para tratamento de exceções, foi configurado para ser invocado em qualquer momento que o usuário informa algo que não corresponde às opções disponíves fazendo com que a intent volte a tentar capturar o slot necessário.

### Slots

* **CategoriaProduto**: serve como uma espécie de variável de controle para a uma a conditional branch da _comprarProdutoIntent_, comparando a opção informada pelo usuário para que seja feito o direcionamento à intent correta.
* **Brinquedo**: Serve para armazenar o estoque de brinquedos e contém sinônimos, usado na _comprarBrinquedoIntent_.
* **Remedio**: Serve para armazenar o estoque de remédios e contém sinônimos, usado na _comprarRemedioIntent_.
* **Animal**: Serve para coletar o tipo do animal e partir dele mostrar opções específicas para a espécie, é usado em todas as intents de compra, agendamento de serviços e também na sessão de dicas.
* **Servico**: Armazena as categorias de serviço ofertas e contém sinônimos para ajudar no tratamento de erros, é usada na _agendarServicoIntent_.
* **Racao**: Armazena os tipos de ração disponíveis para ofertar ao cliente e é usada em _comprarRacaoIntent_.


***
## Desenvolvimento
Com as intents e slots criados, foi implementado uma lógica baseada no uso de conditional branching, pois com isso, o chatbot pode avaliar a intenção do usuário com base em palavras-chave ou frases específicas e, em seguida, direcioná-lo para um conjunto específico de respostas pré-programadas que correspondam àquela intenção, isso ajuda a garantir que o chatbot responda de maneira coerente e forneça informações úteis aos usuários. 

Também foi usado os response cards, para que o chatbot possa fornecer opções para o usuário escolher em vez de simplesmente fornecer uma resposta de texto. Isso ajuda a tornar a interação mais envolvente e intuitiva para o usuário, permitindo que ele selecione facilmente a resposta que melhor corresponde à sua intenção. O desenvolvimento do chatbot seguiu sempre com a premissa de melhor experiência do usuário, com diversas sessões de testes de possíveis entradas que gerariam erro no chatbot.
***
## Integrando ao Slack
Para integração com o Slack, foi
necessário seguir os seguintes passos:  
1 - Inscrever-se no Slack;  
2 - Criar um aplicativo no slack;  
3 - Criar um canal de integração no chatbot;  
4 - Após a criação do canal de integração dentro do chatbot será disponibilizado os seguintes URLs que será necessários para o proceder da integração; 

![print endpoint](https://user-images.githubusercontent.com/80013300/221460663-86a33598-04f0-4a09-9b3e-44c9abfefe42.png)

5 - No aplicativo do Slack é necessário configurar os links disponibilizados no canal de integração do chatbot, inserindo a URL Endpoint na sessão do slack “OAuth & Permissions” e o URL Endpoint OAuth na sessão do slack “Event Subscriptions”;  
6 - Após isso, o app está disponível para ser instalado no workspace.
***
## Acesso à aplicação
Para realizar acesso ao ambiente de utilização do petbot, clique [aqui](https://petbotworkspace.slack.com/apps/A04RU9XEMGQ-petbot?utm_source=in-prod&utm_medium=inprod-link_app_directory-channel_settings-click&tab=settings&next_id=0).
***

## Dificuldades

- Uso dos Session Attributes
- Integração com lambda

***

## Conclusão

O desenvolvimento da avaliação foi concluído com sucesso. Sendo de grande importância para a equipe colocar em prática todos os conceitos estudados durante os cursos da sprint e aprimorar ainda mais o conhecimento voltado para chatbots. Sempre mantendo uma organização como equipe visando o aprendizado e compreensão de todo processo de desenvolvimento do chatbot por parte de todos os integrantes da equipe, com isso, finalizando o projeto de forma satisfatória.

***

## Autores

* [Davi Santos](https://github.com/davi222-santos)
* [Humberto Sampaio](https://github.com/Humbert010)
* [Samara Alcantara](https://github.com/SamaraAlcantara)
