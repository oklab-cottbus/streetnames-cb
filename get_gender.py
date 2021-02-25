import json
import pandas as pd
import requests

base_url = "https://www.wikidata.org/w/api.php"

name = "Douglas Adams"

result = requests.get(base_url, params={"action": "wbsearchentities", "search": name, "language": "de","format":"json"})

id = "Q42"


result = request.get(base_url, params={"action": "wbgetentities", "ids":id "language":"de","format":"json"})
gender_id = "Q6581097"

result = request.get(base_url, params={"action": "wbsearchentities", "search":gender_id "language":"de","format":"json"})
