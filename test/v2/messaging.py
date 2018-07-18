import unittest
from python_optimcios.v2.messaging import Messaging


class TestMessaging(unittest.TestCase):
    def setUp(self):
        self.ob = Messaging()

    def test_o(self):
        self.assertEqual(1, 1)

