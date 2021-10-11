
import datetime
from core.nosql import Table, Query
from core.blocks import Block
from core.transactions import Txion


class Blockchain:
    def __init__(self):
        self._chain = Table('blockchain.json')
        self._txion = Table('transaction')

    def _create_block(self):
        """create a new block"""
        index = len(self._chain.all())
        data = self._txion.all()
        timestamp = datetime.datetime.now().strftime("%d-%m-%y")
        last_hash = self._chain.all()[index - 1]['hash'] if not None else ''

        b = Block(index=index, data=data, timestamp=timestamp, last_hash=last_hash)
        # todo : check validity
        self._chain.insert(b.__repr__())
        return b

    def __get__(self, *args):
        """return block by hash"""
        return 'block'

    def synchronise(self, *args):
        """synchronise blockchain with data"""
        pass

    def exchanges(self, *args, **kwargs):
        """create exchange from the node"""
        expeditor = args[0] if args[0] is not None else None
        to = args[1] if args[1] is not None else None
        obj = args[2] if args[2] is not None else None

        if not expeditor or not to or not obj:
            return 'Error execute exchange.'

        timestamp = datetime.datetime.now().strftime("%d %B %Y %H:%M:%S")
        nounce = self._txion.all()[len(self._txion.all()) - 1]['hash'] if len(self._txion.all()) > 0 else 'empty.nounce'
        tx = Txion(expeditor=expeditor, destinator=to, amount=obj, timestamp=timestamp, nounce=nounce)
        # todo : check validity
        self._txion.insert(tx.__repr__())
        return tx

    def peers_exchanges(self, *args, **kwargs):
        """receiving peers exchanges from network"""
        # todo : check validity of obj before update on node
        print('compute - peers_exhchanges : ' + str(args[0]))

    def consensus(self):
        """how block mined"""
        pass

    def forge(self):
        """mine new block """
        # create new block after PoConsensus
        pass

    def __repr__(self):
        return {'blockchain': self._chain.all()}

    def __str__(self):
        return self.__repr__().__str__()
