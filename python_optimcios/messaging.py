from websocket import create_connection


class messaging:
    def __init__(self, url, channel_id, access_token, count=10):
        try:
            self.url = url
            self.channel = channel_id
            self.token = access_token
            self.connectionCount = self.connectionCountDefine = count
        except Exception as err:
            print("[ ERROR ] Read Value Error")
            print("[ ERROR LOG ] URL:" + url)
            print("[ ERROR LOG ] Channel ID:" + channel_id)
            print("[ ERROR LOG ] Access Token:" + access_token)
            print(err)

    def connection(self, log=False) -> bool:
        try:
            ws_url = self.url + "?" + "channel_id=" + self.channel + "&access_token=" + self.token
            if log:
                print("[ LOG ] Connection URL:" + ws_url)
            self.ws = create_connection(ws_url)
            return True
        except Exception as err:
            print("[ ERROR ] CIOS Messaging Connection Error")
            print(err)
            res = self.__reconnection()
            return res

    def sendMessage(self, message, log=False) -> bool:
        try:
            if log:
                print("[ LOG ] Send Message:" + message)
            self.ws.send(message)
            return True
        except Exception as err:
            print("[ ERROR ] CIOS Messaging Send Error")
            print(err)
            self.ws.close()
            res = self.__reconnection()
            return False

    def receiveMessage(self) -> str:
        try:
            text = self.ws.recv()
            return text
        except Exception as err:
            print("[ ERROR ] CIOS Messaging Receive Error")
            print(err)
            self.ws.close()
            return ""

    def __reconnection(self, log=False) -> bool:
        try:
            ws_url = self.url + "?" + "channel_id=" + self.channel + "&access_token=" + self.token
            if log:
                print("[ LOG ] Connection URL:" + ws_url)
            self.ws = create_connection(ws_url)
            self.connectionCount = self.connectionCountDefine
            return True
        except Exception as err:
            self.connectionCount -= 1
            res = False
            if self.connectionCount > 0:
                res = self.__reconnection(log=log)
            else:
                print("[ ERROR ] Reconnect False")
                exit()
            return res

