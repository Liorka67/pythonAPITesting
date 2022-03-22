import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"

response = requests.get(url)

#print(response.content)

#parse response to json format
json_parser = json.loads(response.text)
#print(json_parser)

#fatch value using json path
firstName = jsonpath.jsonpath(json_parser,'data[2].first_name')
print(firstName[0])

for i in range (0,6):
    firstName = jsonpath.jsonpath(json_parser,'data['+str(i)+'].first_name')
    print((firstName[0]))

#fatch the avatar data
#for i in range (0,6):
#    avatar = jsonpath.jsonpath(json_parser,'data['+str(i)+'].avatar')
#    print((avatar[0]))
