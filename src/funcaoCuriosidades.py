import json 
from random import randint

def lambda_handler(event, context):
    try:
        with open("./data.json", "r") as file:
            data = json.load(file)
    except:
        return {
            "statusCode": 500,
            "body": "Erro ao ler o arquivo JSON"
        }
    
    tipo = event['sessionState']['intent']['slots']['tipo']['value']['interpretedValue'] 
    
    tam = len(data[tipo])

    print("tam = ", tam)

    n = randint(0,tam)
    msg = data[tipo][n-1]

    return {
        "statusCode": 200,
        "body": msg
    }
