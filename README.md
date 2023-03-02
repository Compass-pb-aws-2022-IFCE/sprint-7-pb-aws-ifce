# Avaliação Sprint 7 - Programa de Bolsas Compass UOL / AWS e IFCE

![Logo_CompassoUOL_Positivo](https://user-images.githubusercontent.com/94761781/212589731-3d9e9380-e9ea-4ea2-9f52-fc6595f8d3f0.png)


***

## 📌 Tópicos
- [📝 Descrição do projeto](#📝-descrição-do-projeto)
- [💻 Tecnologias](#💻-tecnologias)
- [🛠 Execução](#🛠-execução)
- [🤝 Conexão com Slack](#conexão-com-slack)
- [🤖Acesso ao chatbot](#🤖-acesso-ao-chatbot)
- [💔 Impedimentos](#💔-impedimentos)
- [👥 Equipe](#👥-equipe)
***

## 💻 Tecnologias

- [Amazon Lex](https://aws.amazon.com/pt/lex/)
- [Slack](https://slack.com/intl/pt-br)


***
## 📝 Descrição do projeto

Foi criado um chatbot baseado em um projeto anterior que seguia um dos problemas propostos para os Clusters Econômicos de Inovação de 2021: A sobrecarga no atendimento ao consumidor em caso de falhas massivas em serviços como o fornecimento de Internet e Energia Elétrica.
<br>
Baseado nessa problemática, criamos a Riri, uma assistente virtual que tem como objetivo auxiliar nos momentos de sobrecarga de atendimentos ao cliente, procurando uma solução rápida para o cliente antes de enviá-lo a um atendente humano quando este estiver disponível.
***

## 🛠 Execução
### Criação do bot na plataforma Amazon Lex
![img](https://imgur.com/2fUn6Kx.png)
![img](https://imgur.com/x6wOu7G.png)
![img](https://imgur.com/F4lbCQM.png)

### Overview das Intents
![img](https://imgur.com/DqCojs0.png)

### Intent Inicial:
![img](https://imgur.com/fRfHocP.png)

### Intent ProblemasInternet:
![img](https://i.imgur.com/6iOJDHn.png)

### Intent TelefoneSemSom
![img](https://i.imgur.com/jghyMYY.png)
![img](https://i.imgur.com/SKQqDFe.png)

### Intent TVaCaboProblems:
![intentTVProblem](https://user-images.githubusercontent.com/119500249/221605831-0a5f9f6b-348c-4b57-94b6-817f214a844a.png)

### Intent PerdaSinalTV:
![IntentPerdaSinalTV](https://user-images.githubusercontent.com/119500249/221606662-54054bc2-7856-4fd8-b1a8-1b3823c45af6.png)

### Intent ImagemCongeladaTV:
![IntentImagemCongelada](https://user-images.githubusercontent.com/119500249/221610031-d10a2ca3-825f-4f66-a7b2-f21df0a66d89.png)

### Intent EncerrarAtendimento
![img](https://i.imgur.com/KqYfZqj.png)

### Intent FallBackIntent
![img](https://imgur.com/imivOa5.png)
***
## Conexão com Slack

Seguindo a documentação para [Integração com Slack](https://docs.aws.amazon.com/pt_br/lex/latest/dg/slack-bot-association.html), conectamos nosso chatbot com a plataforma slack da seguinte forma:

Criação de um canal de integração no Amazon Lex:

![img](https://imgur.com/Dls4BdM.png)
![img](https://imgur.com/yQpsZsx.png)

Abrindo o canal, observamos que são disponibilizados uma URL de Endpoint e uma URL para o Endpoint OAuth:

![img](https://imgur.com/FVnz4Go.png)

Nesta seção, é colocado o ID, segredo e token disponibilizados no Slack ao criar o app na plataforma:

![img](https://imgur.com/Q3zNYU1.png)
![img](https://imgur.com/CpUbEKM.png)

Nas configurações do app Slack, realizamos as seguintes configurações:

Integração do Endpoint OAuth:

![img](https://imgur.com/f99wFex.png)

Integração do Endpoint:

![img](https://imgur.com/HCGgYN5.png)

Adicionando Eventos para requests HTTP/POST:

![img](https://imgur.com/LyNZRqz.png)

Adicionando a aplicação (chatbot) ao Slack

![img](https://imgur.com/z1dneqD.png)

***
## 🤖 Acesso ao chatbot
 O chatbot pode ser acessado através [deste link](https://cariritalk.slack.com/apps/A04S190DXCG-cariritalk2?tab=more_info). Basta clicar no botão "Abrir o Slack" e clicar em "caririTalk" no menu esquerdo para iniciar o chat!
***

## 💔 Impedimentos
- Ativação automática de opções de ganchos de código Lambda nas configurações avançadas de um intent (que não seriam utilizados  durante a criação dos fluxos), gerando erros inesperados.

- Falta de simultaneidade de trabalho: dois membros não conseguiriam trabalhar simultaneamente no chatbot e, portanto era necessário revezar as tarefas, ocupando mais tempo que o ideal

***

## 👥 Equipe

- [Nicolas Ferreira](https://github.com/Niccofs)
- [Jefferson Moreira](https://github.com/Jeef-Moreira)
- [Dayanne Lucy](https://github.com/dayannebugarim)
- [Julio Cesar](https://github.com/JC-Rodrigues)