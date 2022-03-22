import requests
import json
import jsonpath
import openpyxl
from dataDriven import library



def test_add_new_student():
    #Define the URL
    url = 'http://thetestingworldapi.com/api/studentsDetails'
    #Opn file and put it in json format
    f = open('C:/Users/liorkat/Documents/Lior Comp/API Testing/Python/json/studentMultiData.json','r')
    json_format = json.loads(f.read())

    obj = library.common('C:/Users/liorkat/Documents/Lior Comp/API Testing/Python/json/testData.xlsx','Sheet1')
    col = obj.fetch_column_count()
    key = obj.fetch_key_names()
    row = obj.fetch_row_counts()

    for i in range (2,row + 1):
        updated_json_rquest = obj.update_request_with_data(i,json_format,key)
        response = requests.post(url,updated_json_rquest)
        print(response)



