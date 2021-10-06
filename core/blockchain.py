
import datetime
from core.settings import SETTINGS
from core.nosql import Table, Query
from core.objects import Block, Txion


class Blockchain:
    def __init__(self):
        self._chain = Table('blockchain.json')
        self._txion = Table('transaction')

    def _ping(self):
        # send data to peers
        pass

    def pong(self):
        # receiving data from peers
        pass

    def _create_block(self):
        index = len(self._chain.all())
        data = self._txion.all()
        timestamp = datetime.datetime.now().strftime("%d-%m-%y")
        last_hash = self._chain.all()[index - 1]['hash'] if not None else ''

        b = Block(index=index, data=data, timestamp=timestamp, last_hash=last_hash)
        # todo : check validity
        self._chain.insert(b.__repr__())
        self._ping()
        return b

    def exchange(self, *args, **kwargs):
        expeditor = args[0] if args[0] is not None else None
        to = args[1] if args[1] is not None else None
        obj = args[3] if args[3] is not None else None

        if expeditor or to or obj is None:
            return 'Error execute exchange.'

        timestamp = datetime.datetime.now().strftime("%d-%m-%y")
        nounce = self._chain.all()[len(self._chain.all()) - 1]['hash'] if not None else ''
        tx = Txion(expeditor=expeditor, destinator=to, amount=obj, timestamp=timestamp, nounce=nounce)
        # todo : check validity
        self._txion.insert(tx.__repr__())
        self._ping()
        return tx

    def forge(self):
        # create new block after PoConsensus
        pass

    def __repr__(self):
        return {'blockchain': self._chain.all()}

    def __str__(self):
        return self.__repr__().__str__()
