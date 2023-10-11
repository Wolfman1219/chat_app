import requests
import json
import generate_text
from googletrans import Translator
translator = Translator()
url = "https://api.edenai.run/v2/text/topic_extraction"

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYWY3NGIwMjMtNWFhNS00YmRjLThiNjUtMTA4MjlkMWRhZTM2IiwidHlwZSI6ImFwaV90b2tlbiJ9._vY9PWWxSNPUID8KEYNgRc6964ZJaJwWeqZnLuRUCq0"

def get_answer(text_input):
    # text_input = input("Enter your request: ")
    text_input = translator.translate(text_input, dest='en').text
    print(text_input)
    payload = {
        "response_as_dict": True,
        "attributes_as_list": False,
        "show_original_response": False,
        "text": text_input,
        "providers": "openai"
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {token}"
    }

    response = requests.post(url, json=payload, headers=headers)
    response = json.loads(response.text)
    response_cat = response['openai']['items'][0]['category']
    response_topic = response_cat.split("/")
    print(response_topic)
    if "medical" in response_cat.lower():
        return(generate_text.get_chat_answer(text_input))
        
    else:
        return "Your request is invalid"