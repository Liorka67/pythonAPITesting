import json
import jsonpath
import pytest
import requests

url = "https://reqres.in/api/users/2"
a=10
@pytest.fixture
def startExecution():
    global file
    file = open("C:\\Users\\liorkat\\Documents\\Lior Comp\\python\\data\\createUserUpdate.json", "r")


@pytest.mark.smoke
def test_create_new_user(startExecution):
#for the json file

    json_input = file.read()
    response_json = json.loads(json_input)
    print(response_json)
    #make PUT request with json input body
    response = requests.put(url,response_json)
    print(response.content)
    #validating response code different response code
    assert response.status_code == 200
    #parse response content
    response_json = json.loads(response.text)
    print(response_json)
    update_li = jsonpath.jsonpath(response_json,'updatedAt')
    print(update_li)

#TC # 2
@pytest.mark.smoke
def test_create_other_user():
#for the json file

    json_input = file.read(startExecution)
    response_json = json.loads(json_input)
    print(response_json)
    #make PUT request with json input body
    response = requests.put(url,response_json)
    print(response.content)

#TC # 3
def test_create_other_user():
#for the json file
    file = open("C:\\Users\\liorkat\\Documents\\Lior Comp\\python\\data\\createUserUpdate.json","r")
    json_input = file.read()
    response_json = json.loads(json_input)
    print(response_json)
    #make PUT request with json input body
    response = requests.put(url,response_json)
    print(response.content)
