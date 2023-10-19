import json
import requests
from googletrans import Translator
import re
import search_api
import bs4
import urllib.request

translator = Translator()
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMTQxMWQ1N2YtZjMyNC00MjE2LTg0ZDMtY2U2MDBhZDFkODFlIiwidHlwZSI6ImFwaV90b2tlbiJ9.rVFouvlDqOD-DaKG1WhWId5IETCr1k4XNiNb-97rNdw"
headers = {"Authorization": f"Bearer {token}"}

url ="https://api.edenai.run/v2/text/chat"


def get_chat_answer(question, history, global_action):
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
      "chatbot_global_action": global_action,
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
      "chatbot_global_action": global_action,
      "text": text
  }
  response = requests.post(url, json=payload, headers=headers)
  result = json.loads(response.text)
  print(result)
  google_query = re.search(r"<<\^\^\^([\w\s]+)\^\^\^>>", text)
  if google_query:
    extracted_text = google_query.group(1)
    links = search_api.get_results(extracted_text)
    a_website = urllib.request.urlopen(url)
    a_soup = bs4.BeautifulSoup(a_website)
    print(a_soup)
    get_chat_answer(str(a_soup), history, global_action)
  else:
    return result['openai']['generated_text']