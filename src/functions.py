def prepareResponse(event, msgText):
    if isinstance(msgText, list):
        messages = [
            {"contentType": "PlainText", "content": msg} for msg in msgText
        ]
    else:
        messages = [{"contentType": "PlainText", "content": msgText}]
    
    response = {
        "sessionState": {
            "dialogAction": {"type": "Close"},
            "intent": {
                "name": event['sessionState']['intent']['name'],
                "state": "Fulfilled"
            }
        },
        "messages": messages
    }
    
    return response