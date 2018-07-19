from websocket import create_connection
import sys
import urllib.request
import urllib.parse
import json
import time


class Messaging:
    def __init__(self, client_id="", client_secret="", channel_id="", log=False, cnt=3):

        # Data
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = ""
        self.channel_id = channel_id
        self.cios_url = "wss://api.optim.cloud/v2/messaging"
        self.log = log
        print("Log " + str(log))

        # Class Field
        self.ws = ""
        self.connectionCountDefine = self.connectionCount = cnt

        self.__consoleLog("Create Messaging Instance")
        self.__consoleLog("Set Parameters")

    def OAuth(self) -> bool:
        req = self.__OAuthRequestData()

        url = "https://auth.landlog.info/v2/connect/token"
        en_req = urllib.parse.urlencode(req).encode("utf-8")

        self.__consoleLog("OAuth2 Request Url " + url)
        self.__consoleLog("OAuth2 Request Body \n" + json.dumps(req))

        try:
            with urllib.request.urlopen(url, data=en_req) as res:
                res_data = res.read().decode("utf-8")
                self.__consoleLog("OAuth Response Body \n" + res_data)
                d = json.load(res_data)

            self.access_token = d["access_token"]
        except:
            self.__consoleLog("OAuth Access Failure", True)
            sys.exit(1)
        return True

    def connection(self) -> bool:
        try:
            ws_url = self.cios_url + "?" + "channel_id=" + self.channel_id + "&access_token=" + self.access_token
            self.__consoleLog("Connection URL:" + ws_url)
            self.ws = create_connection(ws_url)
            return True
        except Exception as err:
            self.__consoleLog("CIOS Messaging Connection Error", True)
            self.__consoleLog(err, True)
            res = self.__reconnection()
            return res

    def sendMessage(self, message) -> bool:
        try:
            self.__consoleLog("Send Message:" + message)
            self.ws.send(message)
            return True
        except Exception as err:
            self.__consoleLog("CIOS Messaging Send Error", True)
            self.__consoleLog(str(err), True)
            self.ws.close()
            res = self.__reconnection
            return res

    def receiveMessage(self) -> str:
        try:
            text = self.ws.recv()
            return text
        except Exception as err:
            self.__consoleLog("CIOS Messaging Receive Error", True)
            self.__consoleLog(str(err), True)
            self.ws.close()
            return ""

    def __reconnection(self) -> bool:
        try:
            time.sleep(2)
            ws_url = self.cios_url + "?" + "channel_id=" + self.channel_id + "&access_token=" + self.access_token
            self.__consoleLog("Reconnection WebSocket")
            self.__consoleLog("Connection URL:" + ws_url)
            self.ws = create_connection(ws_url)
            self.connectionCount = self.connectionCountDefine
            return True

        except Exception as err:
            self.__consoleLog("Reconnect False", True)
            self.__consoleLog(str(err), True)
            self.__consoleLog("Connection Count :" + str(self.connectionCount), True)
            self.connectionCount -= 1
            res = False
            if self.connectionCount > 0:
                res = self.__reconnection
            else:
                self.__consoleLog("Reconnect False")
                exit()
            return res

    def __consoleLog(self, t, e=False) -> bool:
        if e:
            print("[ ERROR ] " + t)
        elif self.log:
            print("[ LOG ] " + t)
        else:
            return False
        return True

    def __OAuthRequestData(self) -> dict:
        try:
            req = {
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "scope": "messaging.subscribe,messaging.publish"
            }
        except:
            self.__consoleLog("'client_id','client_secret' not found ", True)
            sys.exit(1)
        return req