import jsonpath
import requests
import json
import pjsonpath

def test_add_student_data():
    APIurl = 'http://thetestingworldapi.com/api/studentsDetails'
    f=open('C:/Users/liorkat/Documents/Lior Comp/API Testing/Python/json/studentData.json','r')
    json_request = json.loads(f.read())
    response = requests.post(APIurl,json_request)
    print(response.text)

def test_get_student_data():
    APIurl = 'http://thetestingworldapi.com/api/studentsDetails/1033573'
    response = requests.get(APIurl)
    jsonFormat = json.loads(response.text)
    id = jsonpath.jsonpath(jsonFormat,'data.id')
    print(id)
    assert id[0] == 1033573

def test_update_student_data():
    APIurl = 'http://thetestingworldapi.com/api/studentsDetails/1033573'
    f=open('C://Users//liorkat//Documents//Lior Comp//API Testing//Python//json//studentUpdateData.json','r')
    json_request = json.loads(f.read())
    putResponse = requests.put(APIurl,json_request)
    print(putResponse.status_code)



def test_get_update_student_data():
    APIurl = 'http://thetestingworldapi.com/api/studentsDetails/1033573'
    response = requests.get(APIurl)
    jsonFormat = json.loads(response.text)
    print(jsonFormat)
    lastName = jsonpath.jsonpath(jsonFormat,'data.last_name')
    print(lastName)

