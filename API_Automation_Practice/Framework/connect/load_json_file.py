import json
import requests
# from Framework.basefile import Base_url
#
# url = Base_url
#
# final_url = url.base
# header = url.header

class load_file:
    # def connection(self):
    #     f = open("data.json")
    #     data = json.load(f)
    #     return data
    #     # for i in data['test_data']:
    #     #     # self.response = requests.post(final_url, Headers=header, data=json.dumps(i))
    #     #     yield i
        def __init__(self):
            self.__data = None

        def connect(self, data_file):
            with open(data_file) as json_file:
                self.__data = json.load(json_file)

        def get_data(self):
            for organization in self.__data:
                    # self.response = requests.post(final_url, headers=header.headers,
                    #                               data=json.dumps(organization))
                    yield organization