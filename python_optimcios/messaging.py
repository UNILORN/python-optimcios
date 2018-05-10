from websocket import create_connection


class messaging:
    def __init__(self, url, channel_id, access_token):
        self.url = url
        self.channel = channel_id
        self.token = access_token
        self.ws = 0

    def connection(self)->bool:
        try:
            ws_url = self.url + "?" + "channel_id=" + self.channel + "&access_token=" + self.token
            self.ws = create_connection(ws_url)
            return True
        except Exception as err:
            print("[ ERROR ] CIOS Messaging Connection Error")
            print(err)
            return False

    def sendMessage(self, message)->bool:
        try:
            self.ws.send(message)
            return True
        except Exception as err:
            print("[ ERROR ] CIOS Messaging Send Error")
            print(err)
            self.ws.close()
            return False

    def receiveMessage(self)->str:
        try:
            text = self.ws.recv()
            return text
        except Exception as err:
            print("[ ERROR ] CIOS Messaging Receive Error")
            print(err)
            self.ws.close()
            return ""


