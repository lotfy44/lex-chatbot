import json
import boto3
import os
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
TABLE_NAME = os.environ.get("INTERACTIONS_TABLE", "ChatbotInteractions")
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))
    
    # Extract session state & intent
    session_state = event.get("sessionState", {})
    intent_obj = session_state.get("intent", {})
    intent_name = intent_obj.get("name", "GreetIntent")
    session_id = session_state.get("sessionId", "unknown")
    
    # Extract user message
    user_text = event.get("inputTranscript") or event.get("text", "")
    
    # Save to DynamoDB
    timestamp = datetime.utcnow().isoformat()
    table.put_item(Item={
        "userId": session_id,
        "timestamp": timestamp,
        "intent": intent_name,
        "text": user_text
    })
    
    # Return valid Lex V2 response
    response = {
        "sessionState": {
            "dialogAction": {
                "type": "Close"
            },
            "intent": {
                "name": intent_name,
                "state": "Fulfilled"
            },
            "sessionAttributes": session_state.get("sessionAttributes", {})
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": f"Thanks, I recorded your message: '{user_text}'"
            }
        ]
    }
    
    return response
