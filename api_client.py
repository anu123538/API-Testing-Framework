# utils/api_client.py
import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def get(self, endpoint):
        return self.session.get(self.base_url + endpoint)

    def post(self, endpoint, json=None, headers=None):
       return self.session.post(self.base_url + endpoint, json=json, headers=headers)


    def put(self, endpoint, json=None, headers=None):
       return self.session.put(self.base_url + endpoint, json=json, headers=headers)

    def delete(self, endpoint):
        return self.session.delete(self.base_url + endpoint)
