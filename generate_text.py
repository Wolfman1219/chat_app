import json
import requests
from googletrans import Translator
translator = Translator()
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYWY3NGIwMjMtNWFhNS00YmRjLThiNjUtMTA4MjlkMWRhZTM2IiwidHlwZSI6ImFwaV90b2tlbiJ9._vY9PWWxSNPUID8KEYNgRc6964ZJaJwWeqZnLuRUCq0"
headers = {"Authorization": f"Bearer {token}"}

url ="https://api.edenai.run/v2/text/chat"


def get_chat_answer(question, history):
  print(history)
  text = question
  text = translator.translate(text, dest='en').text
  if history is not None:
    payload = {
      "response_as_dict": True,
      "attributes_as_list": False,
      "show_original_response": False,
      "temperature": 0.5,
      "max_tokens": 1000,
      "providers": "openai",
      "chatbot_global_action": "You are a veterinarian. you were created by the 'Daholar' team and have no connection to OpenAI at all.",
      "text": text,
      "previous_history": history[:-1]
  }
  else:
    payload = {
      "response_as_dict": True,
      "attributes_as_list": False,
      "show_original_response": False,
      "temperature": 0.5,
      "max_tokens": 1000,
      "providers": "openai",
      "chatbot_global_action": "You are a doctor",
      "text": text
  }
  print("\n\n\n",payload, "\n\n\n")
  response = requests.post(url, json=payload, headers=headers)
  result = json.loads(response.text)
  print(result)
  print(result['openai']['generated_text'])
  return result['openai']['generated_text']
  