import json

import requests

url = 'https://httpbin.org/user-agent'


def test_statusCode():
    response = requests.get(url)
    assert response.status_code == 200
    print(response.status_code)



#parser = json.load(response.text)

#print(parser,'user_agent')