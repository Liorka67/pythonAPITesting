import json
import jsonpath
import requests

url = "https://reqres.in/api/users/2"


#for the json file
file = open("C:\\Users\\liorkat\\Documents\\Lior Comp\\python\\data\\createUserUpdate.json","r")

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




