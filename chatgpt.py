from api_key import API_KEY
import requests
import json

def pick_word() -> str:
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    link = 'https://api.openai.com/v1/chat/completions'
    model_id = 'gpt-3.5-turbo'
    message_body = {
        'model': model_id,
        'messages':  [
            {
                'role': 'user',
                'content': 'Me diga uma palavra aleatória da língua portuguesa.'
            }
        ]
    }
    message_body = json.dumps(message_body)

    request = requests.post(link,headers=headers,data=message_body)

    response = request.json()
    word = response['choices'][0]['message']['content']
    
    return word