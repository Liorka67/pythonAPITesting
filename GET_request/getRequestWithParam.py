import requests

param = {'name':'Lior','lastName':'katz','mail':'liorkat@matrix.co.il'}

response = requests.get('https://httpbin.org/get',params=param)

print(response.content,'Host')

