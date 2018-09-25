class Datastore:
    def __init__(self, access_token="",api_uri="", log=False):

        # Data
        self.access_tokne = access_token
        self.api_url = "https://" + api_uri + "/v2/datastore"
        self.log = log



