import unittest
import os
from os.path import dirname, abspath
from dotenv import load_dotenv
from python_optimcios.v2 import messaging, authorization


class TestMessaging(unittest.TestCase):
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

        self.messaging = messaging.Messaging(
            access_token=access_token,
            channel_id=os.environ.get("MESSAGING_CHANNEL_ID"),
            api_uri=os.environ.get("API_URI"),
            log = True
        )

    @unittest.skip("Messaging Channel None")
    def test_WSConnection(self):
        r = self.messaging.connection()
        self.assertEqual(r, True)
