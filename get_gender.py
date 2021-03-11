import json
import traceback
import re
import pandas as pd
import requests


def get_gender(streetname):
  base_url = "https://www.wikidata.org/w/api.php"
  try: 
    name = replace(streetname)
    result = requests.get(base_url, params={"action": "wbsearchentities", "search": name,"limit":"10","language": "de","format":"json"})
    
    for x in result.json()['search']:
      id =  x['id']
    
      result = requests.get(base_url, params={"action": "wbgetentities", "ids":id ,"language":"de","format":"json"})
    
      if result.json()['entities'][id]['claims']['P31'][0]['mainsnak']['datavalue']['value']['id'] == "Q5":

        gender_id = result.json()['entities'][id]['claims']['P21'][0]['mainsnak']['datavalue']['value']['id']
        matched_name = x['label']

        try:
          date_of_birth = result.json()['entities'][id]['claims']['P569'][0]['mainsnak']['datavalue']['value']['time']
        except Exception as e:
          date_of_birth = "NA"

        try:
          date_of_death = result.json()['entities'][id]['claims']['P570'][0]['mainsnak']['datavalue']['value']['time']
        except Exception as e:
          date_of_death = "NA"

        try:  
          description = result.json()['entities'][id]['descriptions']['de']['value']
        except Exception as e:
          description = "NA"

        try:
          ethnic_group_id = result.json()['entities'][id]['claims']['P172'][0]['mainsnak']['datavalue']['value']['id']
        except Exception as e:
          ethnic_group_id = "NA"

        break;
        
    gender_result = requests.get(base_url, params={"action": "wbsearchentities", "search":gender_id, "language":"de","format":"json"})
    
    gender = gender_result.json()['search'][0]['label']
    try:
      ethnic_result =  requests.get(base_url, params={"action": "wbsearchentities", "search":ethnic_group_id, "language":"de","format":"json"})
      ethnic_group = ethnic_result.json()['search'][0]['label']
    except Exception as e:
      ethnic_group = "NA" 
    
  except Exception as e:
    gender = "NA"
    matched_name = "NA"
    description = "NA"
    date_of_birth = "NA"
    date_of_death = "NA"
    ethnic_group = "NA"
    #print(traceback.format_exc())
  row = {"Name":[streetname],
         "Gender":[gender],
         "Information":[description],
         "searched_name":[name],
         "matched_name":[matched_name],
         "date_of_birth":[date_of_birth],
         "date_of_death":[date_of_death],
         "ethnic_group":[ethnic_group]}
  return(row)

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

    
