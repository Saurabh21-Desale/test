import pytest
import json
import requests
#from Framework.connect.load_json_file import load_file
from Framework.basefile.Base_url import Base_url

#file = load_file
url = Base_url

def get_data():
    f = open("C:\\Users\\saurabhd\\PycharmProjects\\API_Automation_Practice\\Framework\\data\\data.json")
    data = json.load(f)
    for i in data['test_data']:
        response = requests.post(url.base, data=json.dumps(i))
        yield i

@pytest.mark.parametrize("test", get_data())
def test_all_data(test):
    print(test)
   # assert file.response.status_code == 200
