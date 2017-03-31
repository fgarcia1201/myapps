import json
from pprint import pprint

with open('file.json') as data_file:
	data = json.load(data_file)

pprint(data["maps"][0]["id"])
