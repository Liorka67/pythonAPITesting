import requests
import json
import jsonpath

def test_getDetialsAPI():
    url = 'https://reqres.in/api/users?page=2'
    response = requests.get(url)
    #print(response.text)

    json_format = json.loads(response.text)
    id = jsonpath.jsonpath(json_format,'data[1],id')

    print(id)