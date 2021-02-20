import json
import pandas as pd
import requests

base_url = "https://www.wikidata.org/w/api.php"

name = "Douglas Adams"

result = requests.get(base_url, params={"action": "wbsearchentities", "search": name, "language": "de","format":"json"})

