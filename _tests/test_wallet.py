
import unittest
from unittest.mock import MagicMock
from core.wallet import Wallet

t_wallet = Wallet()
t_private_key = None
t_secret_phrase = None


class WalletTest(unittest.TestCase):

    def test_create(self):
        t_wallet.create('test')

        self.assertTrue(t_wallet.public_key is not None)
        self.assertTrue(t_wallet.__repr__()['private_key'] is not None)
        self.assertTrue(t_wallet.__repr__()['secret_phrase'] is not None)
        t_private_key = t_wallet.__repr__()['private_key']
        t_secret_phrase = t_wallet.__repr__()['secret_phrase']

    def test_open(self):
        t_wallet.open('test', t_private_key, t_secret_phrase)

        self.assertTrue(t_wallet.public_key is not None)
        self.assertTrue(t_wallet.__repr__()['private_key'] is not None)
        self.assertTrue(t_wallet.__repr__()['secret_phrase'] is not None)
