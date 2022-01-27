
import unittest
from core.blockchain import Blobchain, Block, Txion


class BlockchainTest(unittest.TestCase):

    def test_circulated_coins(self):
        t_blobchain = Blobchain()

        self.assertNotEqual(0, t_blobchain.current_circulated_coins)

    def test_create_block(self):
        t_blobchain = Blobchain()
        t_proof = 23
        t_miner = 'tester'

        t_block = t_blobchain.create_block(t_proof, t_miner)

        self.assertIsNotNone(t_block)
        self.assertEqual(t_proof, t_block.proof)
        self.assertIsNotNone(t_block.hash)

    def test_last_block(self):
        t_blobchain = Blobchain()

        t_res_block = t_blobchain.last_block()

        self.assertIsNotNone(t_res_block)

    def test_get_block(self):
        t_blobchain = Blobchain()
        t_hash = '1eb1c48d7d6fdd9c530c6e9ca3a556cfdbe96101a26554a785ac097f686460ab'

        t_res_block = t_blobchain.block(t_hash)

        self.assertIsNotNone(t_res_block)

    def test_forge(self):
        t_blobchain = Blobchain()
        tester = 'tester_address'

        res = [r for r in t_blobchain.forge(tester)]

        self.assertEqual(type(res[0]), Block)
        self.assertEqual(type(res[1]), Txion)
        self.assertEqual(type(res[2]), int)

    def test_exchanges(self):
        t_blobchain = Blobchain()
        expeditor = 'exp1'
        destinator = 'destinator1'
        amount = 100

        t_res_txion = t_blobchain.exchanges(expeditor, destinator, amount)

        self.assertIsNotNone(t_res_txion)
        self.assertEqual(expeditor, t_res_txion.expeditor)
        self.assertEqual(destinator, t_res_txion.destinator)
        self.assertEqual(amount, t_res_txion.amount)

