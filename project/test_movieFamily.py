import jsonpath
import requests
import json

url = 'https://api.sampleapis.com/movies/drama'

def test_movie():
    response = requests.get(url)
    json_format = json.loads(response.text)
    print(json_format)
    #title = jsonpath.jsonpath(json_format(),'title[0]')
    #print(title)
