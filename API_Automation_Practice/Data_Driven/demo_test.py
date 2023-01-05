import json

import pytest
import requests

f = open('data_driven.json')

# json.loads = takes in a string and returns a json object.
data = json.load(f)

@pytest.mark.parametrize()
def test_data_driven(a):
    for i in data['test_data']:
      # json.dumps = takes in a json object and returns a string.
      res=json.dumps(data, indent=1)
      print(res)
      break
