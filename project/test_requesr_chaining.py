import json
import jsonpath
import requests

def test_add_new_student():
    global id
    API_url = 'http://thetestingworldapi.com/api/studentsDetails'
    f = open('C:/Users/liorkat/Documents/Lior Comp/API Testing/Python/json/addStudent.json','r')
    json_format = json.loads(f.read())
    response = requests.post(API_url,json_format)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])

def test_get_details():
    API_url_get = 'http://thetestingworldapi.com/api/studentsDetails/' + str(id[0])
    response = requests.get(API_url_get)
    print(response.text)


