# 📑 Avaliação Sprint 7 - Programa de Bolsas Compass UOL 
## Finalidade do Projeto
Os chatbots são uma solução cada vez mais popular para melhorar a eficiência e a qualidade do atendimento ao cliente. No caso do setor de TI do Município de Tauá, que recebe diariamente uma grande quantidade de solicitações de suporte técnico por meio do WhatsApp, o uso de um chatbot pode ser transformador.

Com a implementação de um chatbot, as solicitações de suporte técnico podem ser atendidas de forma mais rápida e eficiente. O chatbot pode ser programado para entender e responder automaticamente a uma ampla variedade de solicitações, desde a troca de toner de impressora até o upgrade de computadores.

Isso significa que as solicitações são atendidas em tempo hábil, sem a necessidade de um técnico de TI responder manualmente cada mensagem, o que pode levar muito tempo e deixar o serviço acumulado. Além disso, o chatbot também pode ser programado para oferecer soluções simples e comuns para problemas técnicos, permitindo que os técnicos se concentrem em tarefas mais complexas e de maior valor agregado.

Outra vantagem do uso do chatbot é a sua disponibilidade 24 horas por dia, 7 dias por semana. Isso significa que os usuários podem fazer solicitações a qualquer momento, sem precisar esperar pelo horário de trabalho dos técnicos de TI. Isso é particularmente importante em situações de emergência, como interrupções do serviço ou falhas nos sistemas. 

## Requisitos
- Conta na AWS.
- Conta no Slack.

## Intents
- Setores: Define os setores que compõe a Secretaria de Educação;
- Impressora: Fornece informações para a troca de toner/tinta ou problemas de drives na impressora;
- Internet: Fornece informações quando um setor estar sem internet ou quando danifica algum equipamento;
- Atendimento: Fornece as opções disponíveis para o usuário ter acesso;
- Saudações: Inicía o atendimento ao serviço;
- Impressorafunction
- Documentos: Emite as opções de boletim e histórico;
- FallbackIntent: Tratamento de rede.


## Conexão do Amazon Lex com Slack 
Primeiramente, é necessário criar uma conta no Slack e em seguida, um Workspace. Após isso, é preciso criar uma aplicação Slack no console da API do Slack. Nessa aplicação, é necessário configurar os recursos, tais como Interactivity & Shortcuts e Basic Information, para obter as credenciais do aplicativo que serão utilizadas no Amazon Lex.

Em seguida, é preciso integrar a aplicação Slack com o Amazon Lex Bot. Para fazer isso, é necessário abrir o console do Amazon Lex, selecionar o bot criado e escolher a guia Canais. Em seguida, é preciso selecionar a plataforma Slack, escolher um nome para a integração e digitar as credenciais obtidas no passo anterior.

Depois de concluir a integração, é necessário voltar para a aplicação Slack e atualizar os recursos OAuth & Permissions, Bot Token Scopes, Interactivity & Shortcuts e Event Subscriptions. Por fim, é necessário marcar o checkbox da seção Messages Tab no menu App Home.

Após concluir todos esses passos, é possível testar a integração. No menu Manage Distribution, escolha Add to Slack para instalar a aplicação e forneça as permissões. Em seguida, acesse seu Workspace do Slack e inicie um bate-papo.

Com a integração do Slack com o Amazon Lex, é possível melhorar a comunicação de uma empresa ou organização, tornando-a mais eficiente e rápida. Isso resulta em um melhor atendimento aos clientes e em um ambiente de trabalho mais produtivo.

## Impedimentos
 - Dificuldade em compartilhar o chatbot;

## Acesso ao Chatbot
Para acessar a aplicação [clica nesse link](https://join.slack.com/t/cite-grupo/shared_invite/zt-1qinm3z0j-RCLi3fD5x5wsudHVsclkAQ).
## Equipe
- Rangel Melo.
- Luiz Carlos.
- Tecla Fernandes. 
