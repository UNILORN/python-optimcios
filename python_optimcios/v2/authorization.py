import requests
import urllib.parse
import json


class Authorization:
    def __init__(self, auth_uri="", client_id="", client_secret="", log=False):
        """
        :param auth_uri:
        :param client_id: 
        :param client_secret: 
        :param log: 
        """
        self.auth_url = "https://" + str(auth_uri) + "/connect/token"
        self.client_id = client_id
        self.client_secret = client_secret
        self.log = log

    def getRefreshAccessToken(self, scope="", refresh_token=""):
        """
        :param scope: 
        :param refresh_token: 
        :return: 
        """
        self.__consoleLog("Run getRefreshAccessToken()")

        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "scope": scope
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        self.__consoleLog("Request Data [" + json.dumps(data) + "]")
        self.__consoleLog("Request Header [" + json.dumps(headers) + "")

        res = self.__postAuthorizationData(url=self.auth_url, data=data, headers=headers)

        self.__consoleLog("Get AccessToken [" + res["access_token"] + "]")

        return res["access_token"]

    def __postAuthorizationData(self, url, data, headers):
        """
        :param url: 
        :param data: 
        :param headers: 
        :return: 
        """
        try:
            self.__consoleLog("HTTPRequest :method=POST :url=" + str(url))
            res = requests.post(url=url, data=data, headers=headers)
            self.__errorHandling(res.status_code)
        except:
            self.__consoleLog("POST RequestError",True)
            raise Exception("POST RequestError")
        return res.json()

    def __consoleLog(self, t, e=False) -> bool:
        """
        :param t: text 
        :param e: error
        :return: 
        """
        if e:
            print("[ ERROR ] " + t)
        elif self.log:
            print("[ LOG ] " + t)
        else:
            return False
        return True

    def __errorHandling(self, status_code):
        """
        :param status_code: 
        :return: 
        """
        if not status_code == 200:
            self.__consoleLog("StatusCode Error ["+ str(status_code)+"]", True)
            return Exception("StatusCode [" + str(status_code) + "] Error")
        return True
