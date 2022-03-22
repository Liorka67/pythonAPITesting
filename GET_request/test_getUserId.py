import requests
import json
import jsonpath

url = 'https://reqres.in/api/users?page=2'

response = requests.get(url)

print(response.text)

json_format_file = json.loads(response.text)

print(json_format_file)

val = jsonpath.jsonpath(json_format_file,'data[1].id')

print(val)
print('assert response.url == url')