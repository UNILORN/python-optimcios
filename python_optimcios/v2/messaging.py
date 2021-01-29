from websocket import create_connection
import time


class Messaging:
    def __init__(self, access_token="", channel_id="", api_uri="", log=False, cnt=3):

        # Data
        self.access_token = access_token
        self.channel_id = channel_id
        self.api_url = "wss://" + api_uri + "/v2/messaging"
        self.log = log

        # Class Field
        self.ws = ""
        self.connectionCountDefine = self.connectionCount = cnt

        self.__consoleLog("Create Messaging Instance")
        self.__consoleLog("Set Parameters")

    def connection(self) -> bool:
        try:
            ws_url = self.api_url + "?" + "channel_id=" + self.channel_id + "&access_token=" + self.access_token + "&packer_format=json&mode=pubsub"
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
            ws_url = self.api_url + "?" + "channel_id=" + self.channel_id + "&access_token=" + self.access_token
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
