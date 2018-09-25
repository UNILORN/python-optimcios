import requests
import json


class Datastore:
    def __init__(self, access_token="", api_uri="", log=False):
        # Data
        self.access_token = access_token
        self.api_url = "https://" + api_uri + "/v2/datastore"
        self.log = log

        # AccessToken Setting
        self.headers = {"Authorization": "Bearer " + self.access_token}

    def getListChannel(self, params=None):
        if params is None:
            params = {}

        res = requests.get(
            url=self.api_url + "/channels",
            params=params,
            headers=self.headers
        )

        return res.json()
