
import datetime
import hashlib
import random
from core.nosql import Table, Query
from core.blocks import Block
from core.transactions import Txion
from core.settings import SETTINGS
from core.libs import SingletonMeta


class Blobchain(metaclass=SingletonMeta):
    def __init__(self):
        self._chain = Table('blockchain')
        self._txion = Table('exchanges')

        self._max_coin = SETTINGS.COIN
        self._current_circulated_coins = 0
        self._txion_count = 0
        if len(self._chain.all()) < 1:
            self.create_block(None, None)
        self._circulation()

    @property
    def current_circulated_coins(self):
        return self._current_circulated_coins

    def _circulation(self):
        blocks = self._chain.all()
        for b in blocks:
            if type(b['data']) == list:
                for tx in b['data']:
                    self._txion_count += 1
                    if tx['expeditor'] == SETTINGS.SIGNATURE:
                        self._current_circulated_coins += tx['amount']

    def balance(self, address):
        """ return balance of transactions of a given address """
        tmp_txions = []
        tmp_balance = 0
        # Blocks : valid
        blocks = self._chain.all()
        for b in blocks:
            if type(b['data']) == list:
                for tx in b['data']:
                    if tx['destinator'] == address:
                        tmp_balance += tx['amount']
                        tmp_txions.append(tx)
        # Transactions : opened
        txions = self._txion.all()
        for t in txions:
            if t['destinator'] == address:
                tmp_balance += t['amount']
                tmp_txions.append(t)

        return tmp_balance, tmp_txions

    def create_block(self, proof, miner):
        """create a new block"""
        index = len(self._chain.all())
        data = self._txion.all() if index > 0 else {'describe': '# genesis blob of the chain',
                                                    'NAME': SETTINGS.NAME,
                                                    'SIGNATURE': SETTINGS.SIGNATURE,
                                                    'NETWORK': SETTINGS.NETWORK,
                                                    'COIN_NAME': SETTINGS.COIN_NAME,
                                                    'COIN': SETTINGS.COIN}
        timestamp = datetime.datetime.now().strftime(" %d/%m/%Y_%H:%M:%S")
        last_hash = self._chain.all()[index - 1]['hash'] if len(self._chain.all()) > 0 else '[GENESIS_BLOB_0111]'
        forge_by = miner if len(self._chain.all()) > 0 else SETTINGS.SIGNATURE
        b = Block(index=index, data=data, proof=proof, timestamp=timestamp, last_hash=last_hash, forge_by=forge_by)

        self._chain.insert(b.__repr__())
        self._txion.truncate()
        return b

    def last_block(self):
        """ return last_block of the chain """
        return self._chain.all()[len(self._chain.all()) - 1]

    def block(self, *args):
        """ returning block by hash"""
        b = Query()
        return self._chain.search(b.hash == args[0])[0] if len(self._chain.search(b.hash == args[0])) > 0 else 'None'

    def _reward(self, address):
        """ calculate and distribute rewards after forging block """
        guess_rewards = random.randint(SETTINGS.REWARD_MIN, SETTINGS.REWARD_MAX)
        rewarded_tx = self.exchanges(SETTINGS.SIGNATURE, address, guess_rewards)
        self._current_circulated_coins += guess_rewards
        return rewarded_tx

    def forge(self, miner):
        """ creating new block by forging()"""

        def valid_proof(last_proof, guessing_value, last_hash):
            """
            Validates the Proof
            :param last_proof: <int> Previous Proof
            :param guessing_value: <int> Current Proof
            :param last_hash: <str> The hash of the Previous Block
            :return: <bool> True if correct, False if not.
            """

            guess = f'{last_proof}{guessing_value}{last_hash}'.encode()
            guess_hash = hashlib.sha256(guess).hexdigest()
            return guess_hash[:4] == "0000"

        def proof_of_work(last_block):
            """
            Simple Proof of Work Algorithm:
             - Find a number p' such that hash(pp') contains leading 4 zeroes
             - Where p is the previous proof, and p' is the new proof

            :param last_block: <dict> last Block
            :return: <int>
            """

            last_proof = last_block['proof']
            last_hash = last_block['hash']

            guessing_proof = 0
            while valid_proof(last_proof, guessing_proof, last_hash) is False:
                guessing_proof += 1

            return guessing_proof

        proof = proof_of_work(self.last_block())
        if proof is not None:
            yield self.create_block(proof, miner)
            yield self._reward(miner)
            yield proof
      
    def synchronise(self, *args, **blockchain):
        """synchronise node with test_network"""
        print('{0} - '.format(args[0]) + str(blockchain))

        resolve = False
        longer_is_self = False
        self_chain = self._chain.all()
        resolve_chain = []

        if args[0] == 'synchronisation':

            def check_blocks_by_hash(longer_chain, other_chain):
                refined_chain = []

                for i in range(len(longer_chain)):
                    b0 = longer_chain[i]
                    b1 = other_chain[i]

                    if b0['last_hash'] == b1['last_hash'] and b0['hash'] == b1['hash']:
                        refined_chain.append(b0)
                    elif b0['last_hash'] == b1['last_hash'] and b0['hash'] != b1['hash']:
                        refined_chain.append(b0)
                        refined_chain.append(b1)
                    elif b0['last_hash'] != b1['last_hash'] and b0['hash'] == b1['hash']:
                        refined_chain.append(b0)
                    elif b0['last_hash'] != b1['last_hash'] and b0['hash'] != b1['hash']:
                        refined_chain.append(b0)
                        refined_chain.append(b1)

                return refined_chain

            self_chain = self_chain.sort()
            network_chain = blockchain['data'].sort()

            if len(self_chain) >= len(blockchain):
                longer_is_self = True

            resolve_chain = check_blocks_by_hash(self_chain, network_chain) if longer_is_self else check_blocks_by_hash(
                network_chain, self_chain)

            if len(resolve_chain) > len(self_chain if longer_is_self else network_chain):
                resolve = True
                self._chain.truncate()
                for it in resolve_chain:
                    self._chain.insert(it)
            else:
                if not longer_is_self:
                    resolve = True

                    self._chain.truncate()
                    for it in resolve_chain:
                        self._chain.insert(it)

            if resolve:
                self.forge(SETTINGS.SIGNATURE)

        elif args[0] == 'resolve':
            resolve = False

            self._chain.truncate()
            for it in resolve_chain:
                self._chain.insert(it)

        else:
            print('Error !')
      
        self._circulation()
        return resolve, resolve_chain

    def exchanges(self, *args):
        """create exchange from the node"""
        expeditor = args[0] if args[0] is not None else None
        to = args[1] if args[1] is not None else None
        obj = args[2] if args[2] is not None else None

        if not expeditor or not to or not obj:
            return 'Error execute exchange.'

        timestamp = datetime.datetime.now().strftime("%d %B %Y %H:%M:%S")
        nounce = self._txion.all()[len(self._txion.all()) - 1]['hash'] if len(self._txion.all()) > 0 \
            else '#0'
        self._txion_count += 1
        tx = Txion(
            expeditor=expeditor,
            destinator=to,
            amount=obj,
            timestamp=timestamp,
            nounce=nounce,
            index=self._txion_count
        )
        self._txion.insert(tx.__repr__())
        return tx

    def peers_exchanges(self, b_type, item):
        """receiving peers exchanges from test_network"""
        print('compute - peers_exchanges : ' + str(b_type))
        if b_type == 'block':
            b = Block(**item)
            self._txion.truncate()
            self._chain.insert(b.__repr__())
        elif b_type == 'txion':
            tx = Txion(**item)
            self._txion.insert(tx.__repr__())

        elif b_type is None:
            print(item)
        else:
            print('unknown item.')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._chain.close()
        self._txion.close()

    def __repr__(self):
        return {'blockchain': self._chain.all()}

    def __str__(self):
        return self.__repr__().__str__()
