from websocket import create_connection
import urllib.request
import urllib.parse
import json
import time


class Messaging:
    def __init__(self, client_id="", client_secret="", channel_id="", log=False):
        self.__consoleLog("Create Messaging Instance")
        self.__consoleLog("Set Parameters")
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = ""
        self.channel_id = channel_id
        self.cios_url = "wss://api.optim.cloud/v2/messaging"
        self.log = log
        print("Log " + str(log))

    def OAuth(self) -> bool:
        req = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "scope": "messaging.subscribe,messaging.publish"
        }
        url = "https://auth.landlog.info/v2/connect/token"
        req = urllib.parse.urlencode(req).encode("utf-8")

        self.__consoleLog("OAuth2 Request Url " + url)
        self.__consoleLog("OAuth2 Request Body \n" + json.dumps(req))

        with urllib.request.urlopen(url, data=req) as res:
            res_data = res.read().decode("utf-8")
            self.__consoleLog("OAuth Response Body \n" + res_data)
            d = json.load(res_data)

        self.access_token = d["access_token"]
        return True

    def connection(self) -> bool:
        pass

    def __consoleLog(self, t, e=False) -> bool:
        if e:
            print("[ ERROR ] " + t)
        elif self.log:
            print("[ LOG ] " + t)
        else:
            pass
