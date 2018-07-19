import unittest
import os
from os.path import dirname, abspath
from dotenv import load_dotenv
from python_optimcios.v2.messaging import Messaging


class TestMessaging(unittest.TestCase):
    def setUp(self):
        dotenv_path = abspath(dirname(__file__) + '../../.env')
        load_dotenv(dotenv_path)
        client_id = os.environ.get("CLIENT_ID")
        client_secret = os.environ.get("CLIENT_SECRET")
        self.ob = Messaging(client_id=client_id, client_secret=client_secret, log=True)

    def test_OAuthConnection(self):
        r = self.ob.OAuth()
        self.assertEqual(r, True)

    def test_WSConnection(self):
        self.ob.OAuth()
        r = self.ob.connection()
        self.assertEqual(r, True)
