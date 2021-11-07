
import datetime
from core.nosql import Table, Query
from core.blocks import Block
from core.transactions import Txion


class Blockchain:
    def __init__(self):
        self._chain = Table('blockchain')
        self._txion = Table('exchanges')

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

    def block(self, *args):
        b = Query()
        return self._chain.search(b.hash == args[0])[0] if len(self._chain.search(b.hash == args[0])) > 0 else 'None'

    def forge(self):
        """ creating new block by consensus"""
        pass

    def synchronise(self, **blockchain):
        """synchronise node with network"""
        print('compute - synchronisation : ' + str(blockchain))
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
        print('compute - peers_exchanges : ' + str(args[0]))

    def __repr__(self):
        return {'blockchain': self._chain.all()}

    def __str__(self):
        return self.__repr__().__str__()
