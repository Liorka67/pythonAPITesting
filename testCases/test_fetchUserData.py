import requests
import pytest

#API URL
url = "https://reqres.in/api/users?page=2"

@pytest.mark.sanity
def test_fetchUserData():
    #Send get request
    response = requests.get(url)
    #Dsplay response content body
    print(response.content)
    # print response value
    print(response)
    #validate status code
    print(response.status_code)
    assert response.status_code == 200
    #Dsplay response content header
    print(response.headers)
    print(response.headers.get('Date'))
    print(response.headers.get('Connection'))
    #Fetch cookies
    print(response.cookies)
    #Fetch Encoding
    print(response.encoding)
    print(response.elapsed)