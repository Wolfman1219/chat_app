import requests
import re
import pandas as pd

def clean_filename(filename):
    filename = re.sub(r'[\\/*?:"<>|]', "", filename)
    return filename

def build_payload(query,start = 1, num = 10, date_restrict = 'm1', **params):
    payload = {
        'key':API_KEY,
        'q': query,
        'cx': start,
        'num': num,
        'date_restrict': date_restrict
    }

    payload.update(params)
    return payload

def make_request(payload):
    response = requests.get('https://www.googleapis.com/customsearch/v1',params=payload)
    if response.status_code != 200:
        raise Exception('Google Custom Search Failed')
    return response.json()

def main(query,result_total =10):
    items = []
    reminder = result_total % 10
    if reminder > 0:
        pages = (result_total // 10) + 1
    else:
        pages = result_total // 10
    for i in range(pages):
        if pages == i + 1 and reminder > 0:
            payload = build_payload(query, start=(i+1)*10, num=reminder)
        else:
            payload = build_payload(query, start=(i+1)*10)
        response = make_request(payload)
        items.extend(response["items"])
    query_string_clean = clean_filename(query)
    df = pd.json_normalize(items)
    df.to_excel("Google Search Result_{0}.xlsx".format(query_string_clean), index=False)

script = '<script async src="https://cse.google.com/cse.js?cx=c11340b43f1204f44"> \
</script> \
<div class="gcse-search"></div>'

if __name__ == '__main__':
    API_KEY = ' AIzaSyDXRqqPV3Lgrdnrb-lkjjdIx5Ck8Y6JQcw'
    ENGINE_ID = 'c11340b43f1204f44'
    search_query = "ChatGPT"
    totaal_results = 35
    main(search_query, totaal_results)