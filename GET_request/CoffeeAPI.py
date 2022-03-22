import jsonpath
import requests
import json

url = 'https://api.sampleapis.com/codingresources/codingResources'

response = requests.get(url)

print(response.status_code)

json_parser = json.loads(response.text)

description = jsonpath.jsonpath(json_parser,'data[1].description')

print(description[0])
