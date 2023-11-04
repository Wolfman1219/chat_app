import json
import requests
from googletrans import Translator
# import re
# import search_api
# import bs4
# import urllib.request
# import get_text_with_site
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
      "max_tokens": 3000,
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
      "max_tokens": 3000,
      "providers": "openai",
      "chatbot_global_action": global_action,
      "text": text
  }
  response = requests.post(url, json=payload, headers=headers)
  result = json.loads(response.text)
  # print(result)
  # google_query = re.search(r"<<\^\^\^([\w\s]+)\^\^\^>>", result['openai']['generated_text'])
  # if google_query:
  #   extracted_text = google_query.group(1)
  #   links = search_api.get_results(extracted_text)
  #   try:
  #     site_text = get_text_with_site.get_text(links[0])
  #     summary = get_text_with_site.get_summary(site_text)
  #     print(summary)
  #     get_chat_answer(summary, history, global_action)
  #   except Exception as e:
  #     print(e)
  # else:
  return translator.translate(result['openai']['generated_text'], dest='uz').text