import json
import re
import pandas as pd
import requests


def get_gender(name):
  base_url = "https://www.wikidata.org/w/api.php"
  try: 
    name = replace(name)
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
    
    
  except Exception as e:
    gender = "NA"
    name_used = "NA"

  return(list[name,gender,name_used])
def test():

  names = pd.read_csv("names-magdeburg.csv")
  print(names)
  for name in names["Name"]:

    print(get_gender(name))


def replace(name):

  suffix = ["Straße","Weg","Am ","Chausse","Im ","An ","Platz","Zum ","Im ","Zur ","Kleine ","Ring","Siedlung"]

  for string in suffix:

    name = re.sub("(?i)"+string,"",name)
    name = re.sub("-"," ",name)

  return(name)

    
