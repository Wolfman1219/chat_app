import requests
import json
from googletrans import Translator
translator = Translator()
class CustomNER:
    def __init__(self):
        self.api = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYWZmNTg4OTUtYmMwZi00YjY1LThhODEtYmMzOTEzYTUyM2JiIiwidHlwZSI6ImFwaV90b2tlbiJ9.D5VrrUkDcO8oIrlslxNkmy7tgG6SAaoP_qNcN0SBRok"
        self.url = "https://api.edenai.run/v2/text/custom_named_entity_recognition"

    def classify(self,text):
        question = translator.translate(text, ds = 'en').text
        print("\n\n\n", question, "\n\n\n")
        
        payload = {
        "response_as_dict": True,
        "attributes_as_list": True,
        "show_original_response": False,
        "entities": ["medical", "person"],
        "providers": "openai",
        "fallback_providers": None,
        "text": question
        }

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Bearer {self.api}"
        }

        response = requests.post(self.url, json=payload, headers=headers)
        print("\n\n\n", response.text,"\n\n\n")
        result = json.loads(response.text)

        entity = result['openai']['entity']
        category = result['openai']['category']
        cat = {}
        for i in category:
            cat[i].app
        
        # return (person, medical)

object = CustomNER()
text = "Men kasalman, menga dori kerak. Mening ukam ham kasal, lekin unga dori yordam bermaydi."

answer = object.classify(text)
if all(answer):
    pass
    # person, medical = object.classify(answer)

    # TO DO
else:
    print("Ushbu mavzu bola kasalliklaridan yiroq")