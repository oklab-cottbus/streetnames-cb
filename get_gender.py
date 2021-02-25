import json
import pandas as pd
import requests

base_url = "https://www.wikidata.org/w/api.php"

name = "Douglas Adams"

result = requests.get(base_url, params={"action": "wbsearchentities", "search": name, "language": "de","format":"json"})

id = result.json()['search'][0]['id']

result = requests.get(base_url, params={"action": "wbgetentities", "ids":id ,"language":"de","format":"json"})

gender_id = result.json()['entities'][id]['claims']['P21'][0]['mainsnak']['datavalue']['value']['id']

result = requests.get(base_url, params={"action": "wbsearchentities", "search":gender_id, "language":"de","format":"json"})

gender = result.json()['search'][0]['label']

print(gender)


