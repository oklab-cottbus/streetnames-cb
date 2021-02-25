import json
import pandas as pd
import requests

base_url = "https://www.wikidata.org/w/api.php"

name = "martin"

result = requests.get(base_url, params={"action": "wbsearchentities", "search": name,"limit":"50","language": "de","format":"json"})

for x in result.json()['search']:
  id =  x['id']

  result = requests.get(base_url, params={"action": "wbgetentities", "ids":id ,"props":"claims","language":"de","format":"json"})

  if result.json()['entities'][id]['claims']['P31'][0]['mainsnak']['datavalue']['value']['id'] == "Q5":

    gender_id = result.json()['entities'][id]['claims']['P21'][0]['mainsnak']['datavalue']['value']['id']
    name_used = x['label'] 
    break;
    
result = requests.get(base_url, params={"action": "wbsearchentities", "search":gender_id, "language":"de","format":"json"})

gender = result.json()['search'][0]['label']

print(gender+";"+name_used)


