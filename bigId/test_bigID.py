import json
import requests
import jsonpath
from urllib3.exceptions import InsecureRequestWarning

endPoint = 'sessions'

def test_createToken():
    api_url = 'https://34.206.5.199/api/v1/' + endPoint
    f = open('C:/Users/liorkat/Documents/Lior Comp/API Testing/Python/json/bigid.json')
    json_file = json.loads(f.read())
    # Suppress only the single warning from urllib3 needed.
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

    response = requests.post(api_url, json_file,verify=False)
    #print(response.text)
    token_value = jsonpath.jsonpath(response.json(), 'auth_token')
    print(token_value)

    auth = {'Authorization': token_value[0]}
    endPoint1 = 'scans'
    api_url_get = 'https://34.206.5.199/api/v1/' + endPoint1
    # Suppress only the single warning from urllib3 needed.
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    response = requests.get(api_url_get, headers=auth,verify=False)
    print(response.text)




