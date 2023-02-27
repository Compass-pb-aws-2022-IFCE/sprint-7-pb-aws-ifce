import json
import boto3
from functions import prepareResponse

lambda_client = boto3.client('lambda')

def responseCard(event, context):
    # Faz alguma lógica com base na entrada do usuário
    message = "sucesso"
    # Cria uma resposta que será enviada de volta para o Amazon Lex V2
    response = {
          "sessionState": {
            "dialogAction": {
              "type": "Close"
            },
            "intent": {
              "name": event['sessionState']['intent']['name'],
                  "state": "Fulfilled"
            }
          },
          "messages": [
           {
            "contentType": "ImageResponseCard",
            "imageResponseCard": {
                "title": "Quem é esse pokemon",
                "imageUrl": "https://polly-spint6.s3.amazonaws.com/pikachu.jpg",
                "buttons": [
                {
                    "text": "bubassauro",
                    "value": "bubassauro"
                },
                {
                    "text": "pikachu",
                    "value": "pikachu"
                }
                ]
            }
            }
           ]
       }
     
    return response


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
