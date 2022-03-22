import requests
import json
import jsonpath

def test_end_to_end():
    APIurl = 'http://thetestingworldapi.com/api/studentsDetails'
    f = open('C:/Users/liorkat/Documents/Lior Comp/API Testing/Python/json/studentData.json','r')
    json_format = json.loads(f.read())
    response = requests.post(APIurl,json_format)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])

    #add technical details
    tech_api_url = 'http://thetestingworldapi.com/api/technicalskills'
    f=open('C:/Users/liorkat/Documents/Lior Comp/API Testing/Python/json/technicalDetails.json','r')
    json_format = json.loads(f.read())
    json_format['id'] = int(id[0])
    json_format['st_id'] = id[0]
    response = requests.post(tech_api_url,json_format)

    #add address details
    addess_api_url = 'http://thetestingworldapi.com/api/addresses'
    f=open('C:/Users/liorkat/Documents/Lior Comp/API Testing/Python/json/adressDetail.json','r')
    json_format = json.loads(f.read())
    json_format['st_id'] = id[0]
    response = requests.post(addess_api_url,json_format)

    #get final details
    final_details_url = 'http://thetestingworldapi.com/api/FinalStudentDetails/'+ str(id[0])
    response = requests.get(final_details_url)
    print(response.text)


