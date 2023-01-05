import json

import requests

url = "http://10.0.2.46:8080/project/add"

header = {

    "Content-Type": "application/json"
}

# open file
f = open('data_driven.json')

# json.loads = takes in a string and returns a json object.
data = json.load(f)


def test_data_driven():
    for i in data['test_data']:
        # if i["ProjectId"] == "101":
        #print(i)
        response = requests.post(url, headers=header, data=json.dumps(i))
        # # json.dumps = takes in a json object and returns a string.
        print(response)
        # #response_body1=response.text # to take response in text formate
        response_body = response.json() # to take response in json formate
        # #print(response_body1)
        print(response_body)
