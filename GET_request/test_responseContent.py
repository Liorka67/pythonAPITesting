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
pages = jsonpath.jsonpath(json_parser,'total_pages')
assert  pages[0] ==2
