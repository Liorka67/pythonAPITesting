import requests

headerData = {'k1' : 'first header', 'T2' : 'second header'}

response = requests.get('https://httpbin.org/get',headers=headerData)
print(response.text)

#responseHeaders = requests.get('https://httpbin.org/get',headerData)

#print(responseHeaders)