import unittest
import os
from os.path import dirname, abspath
from pprint import pprint
import json

from dotenv import load_dotenv
from python_optimcios.v2 import authorization, datastore


class TestDatastore(unittest.TestCase):
    def setUp(self):
        dotenv_path = abspath(dirname(__file__) + '../../.env')
        load_dotenv(dotenv_path)

        scope = "openid profile email address user.profile user.read user.write group.read group.write group.relation.read group.relation.write corporation.read corporation.write corporation.user.read corporation.user.write corporation.group.read corporation.group.write license.read license.write resource_owner.read resource_owner.write acl.read acl.write oauth2_client.write channel_protocol.read channel.read channel.write messaging.subscribe messaging.publish datastore.read datastore.write datastore.upload datastore.download file_storage.read file_storage.write file_storage.upload file_storage.download device.read device.write geo.area.read geo.area.write geo.area-kind.read geo.area-kind.write geo.area.content.write geo.circle.read geo.circle.write geo.map.read geo.map.write geo.point.read geo.point.write geo.polygon.read geo.polygon.write geo.route.read geo.route.write oauth2_client.read"

        auth = authorization.Authorization(
            auth_uri=os.environ.get("AUTH_URI"),
            client_id=os.environ.get("CLIENT_ID"),
            client_secret=os.environ.get("CLIENT_SECRET")
        )
        access_token = auth.getRefreshAccessToken(
            scope=scope,
            refresh_token=os.environ.get("REFRESH_TOKEN")
        )
        self.datastore = datastore.Datastore(
            access_token=access_token,
            api_uri=os.environ.get("API_URI"),
            log=True
        )

    def test_getListChannel(self):
        r = self.datastore.getListChannel()
        self.assertFalse("errors" in r)

    def test_getChannel(self):
        r = self.datastore.getChannel(channel_id=os.environ.get("DATASTORE_CHANNEL_ID"))
        self.assertFalse("errors" in r)

    @unittest.skip("Delete Channel Skip")
    def test_deleteChannel(self):
        pass

    def test_getListObjects(self):
        r = self.datastore.getListObjects(channel_id=os.environ.get("DATASTORE_CHANNEL_ID"))
        self.assertFalse("errors" in r)

    def test_getObject(self):
        r = self.datastore.getObject(channel_id=os.environ.get("DATASTORE_CHANNEL_ID"),object_id=os.environ.get("DATASTORE_OBJECT_ID"))
        self.assertFalse("errors" in r)

    def test_createObject(self):
        r = self.datastore.postObject(channel_id=os.environ.get("DATASTORE_CHANNEL_ID"),data=json.dumps({"message":"test"}))
        self.assertFalse("errors" in r)

    @unittest.skip("Delete Object Skip")
    def test_deleteObject(self):
        pass

    @unittest.skip("")
    def test_getLatestObject(self):
        pass




