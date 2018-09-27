import requests


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
        return self.__toJson(res)

    def getChannel(self, channel_id="", params=None):
        if params is None:
            params = {}

        res = requests.get(
            url=self.api_url + "/channels/" + channel_id,
            params=params,
            headers=self.headers
        )
        return self.__toJson(res)

    def getListObjects(self, channel_id="", params=None):
        if params is None:
            params = {}

        res = requests.get(
            url=self.api_url + "/channels/" + channel_id + "/objects",
            params=params,
            headers=self.headers
        )
        return self.__toJson(res)

    def postObject(self, channel_id="", data="", params=None):
        if params is None:
            params = {}
        headers = {"Content-Type": "application/json"}
        headers.update(self.headers)

        res = requests.post(
            url=self.api_url + "/channels/" + channel_id + "/objects",
            data=data,
            params=params,
            headers=headers
        )
        return self.__toJson(res)

    def getObject(self, channel_id="", object_id="", params=None):
        if params is None:
            params = {}

        res = requests.get(
            url=self.api_url + "/channels/" + channel_id + "/objects/" + object_id,
            params=params,
            headers=self.headers
        )
        return self.__toJson(res)

    def __toJson(self, res):
        if res.status_code == 200:
            return res.json()
        if "errors" in res.json():
            return res.json()
        else:
            return {"errors": [res.json()]}
