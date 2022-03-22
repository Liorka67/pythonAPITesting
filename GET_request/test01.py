import jsonpath
import requests
import json



url = 'https://reqres.in/api/users/2'

def test_getResponse01(url):
    request_response = requests.get(url)
    request_parser = json.loads(request_response.text)
#print(request_parser)
    data = jsonpath.jsonpath(request_parser,'data.first_name')
    return data
#print(data)

valgetResponse001 = getResponse01('https://reqres.in/api/users/2')

print(valgetResponse001)

#def getResponse002(url):
#    requests_respose002 = requests.get(url)
#    request_parser002 = json.loads(requests_respose002.text)

#    data002 = jsonpath.jsonpath(request_parser002,'')



