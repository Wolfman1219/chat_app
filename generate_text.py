import json
import requests
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYWY3NGIwMjMtNWFhNS00YmRjLThiNjUtMTA4MjlkMWRhZTM2IiwidHlwZSI6ImFwaV90b2tlbiJ9._vY9PWWxSNPUID8KEYNgRc6964ZJaJwWeqZnLuRUCq0"
headers = {"Authorization": f"Bearer {token}"}

url ="https://api.edenai.run/v2/text/chat"


def get_chat_answer(question):
  text = question
  payload = {
        "providers": "openai",
        "text": text,
        "chatbot_global_action": "Act as an assistant",
        "previous_history" : [],
        "temperature" : 0.5,
        "max_tokens" : 150
      }
  response = requests.post(url, json=payload, headers=headers)
  result = json.loads(response.text)
  print(result['openai']['generated_text'])
  return result['openai']['generated_text']
  