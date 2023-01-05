import json
import pytest

def get_data():
    f = open("data_driven.json")
    data = json.load(f)
    for i in data['test_data']:
        yield i

@pytest.mark.parametrize("test_input", get_data())
def test_for_all_data(test_input):
    print(test_input)