import urllib.request
import urllib.parse
import json


class Authorization:
    def __init__(self, auth_uri="", client_id="", client_secret=""):
        self.auth_url = "https://" + auth_uri + "/connect/token"
        self.client_id = client_id
        self.client_secret = client_secret

    def getRefreshAccessToken(self, scope="", refresh_token=""):
        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "scope": scope
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        req = urllib.request.Request(self.auth_url, urllib.parse.urlencode(data), headers)
        with urllib.request.urlopen(req) as res:
            body = res.read()

        json_res = json.loads(body)

        # TODO ErrorHandling

        return json_res.access_token
