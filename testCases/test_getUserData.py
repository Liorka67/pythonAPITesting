import requests
import json
import jsonpath

url = 'https://reqres.in/api/users?page=2'

getResponse = requests.get(url)
jsonParser = json.loads(getResponse.text)
id = jsonpath.jsonpath(jsonParser,'data[0].id')

print(id)
