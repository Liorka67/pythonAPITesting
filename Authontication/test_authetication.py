import requests
import json
import jsonpath




def test_autho():
    token_url = 'http://thetestingworldapi.com/Token'
    data = {'grant_type':'password','username':'admin','password':'adminpass'}
    response = requests.post(token_url,data)
    print(response.text)
    token_value = jsonpath.jsonpath(response.json(),'access_token')
    print(token_value)
    auth = {'Authorization':'Bearer' + token_value[0]}
    authoURL = 'http://thetestingworldapi.com/api/StDetails/1104'
    response = requests.get(authoURL,headers=auth)
    print(response.text)
