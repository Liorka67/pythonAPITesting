import requests
from requests.auth import HTTPBasicAuth

def test_basic_authontication():
    athonticationURL = 'https://app.testim.io/#/signin'
    response = requests.get(athonticationURL,auth=HTTPBasicAuth('liorkat@matrix.co.il','G5@EmAB7JhzpR7C'))
    print(response.text)
