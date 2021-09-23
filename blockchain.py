
import datetime
from core.nosql import Table, Query
from core.blockchain.objects import Block, Txion, Telegraph

NETWORK = []
MAX_COIN = 21000000000
REWARD = 10


class Blockchain:
    def __init__(self):
        self._storage = Table('blockchain.json')
        self._chain_infos = {'id': 'index',
                             'block_index': 0,
                             'txion_index': 0,
                             'telegraph_index': 0}
        self._cache_exchanges = []

    def _save_chain_infos(self):
        query = Query()
        self._storage.upsert(self._chain_infos, query.id == 'index')

    def new_block(self, **kwargs):
        query = Query()
        index = len(self._storage.all())
        last_block_hash = self._storage.search(query.id == index - 1)[0]['hash']

        current_block = Block(index=index,
                              data=kwargs['data'],
                              timestamp=kwargs['timestamp'],
                              last_hash=last_block_hash)
        current_block.data = self._cache_exchanges
        self._storage.insert(current_block.__repr__())

        self._chain_infos['block_index'] = index
        self._save_chain_infos()
        self._cache_exchanges.clear()

        self.relay_to(NETWORK, current_block)

    def get_block(self, **kwargs):
        query = Query()
        if 'index' in kwargs.keys():
            return self._storage.search(query.index == kwargs['index'])[0]
        elif 'hash' in kwargs.keys():
            return self._storage.search(query.index == kwargs['hash'])[0]
        else:
            return None

    """ Envoie le nouveau block au réseau """
    @staticmethod
    def relay_to(cible, data):

        def send_to_node(target, value):
            # TODO : Envoie via le réseau
            pass

        if cible is not NETWORK:
            send_to_node(cible, data)
        else:
            for n in NETWORK:
                send_to_node(n, data)

    def relay_from(self, data):
        self._storage.insert(data)
        # TODO : Si c'est un block synchroniser la chaine | Mettre à jour les données de la chaine

    """ Détermine la création des blocks """
    def block_protocol(self):
        pass

    """ Synchronise la chaine avec le réseau """
    def synchronisation(self):
        pass

    """ Envoi de coin ou de telegraph sur le réseau """
    def transfer(self, kwargs):
        if 'amount' in kwargs:
            current_txion = Txion(index=self._chain_infos['txion_index'],
                                  expeditor=kwargs['expeditor'],
                                  destinator=kwargs['destinator'],
                                  amount=int(kwargs['amount']),
                                  timestamp=datetime.datetime.now().strftime('%a, %d %b %Y %H:%M:%S'))

            self._cache_exchanges.append(current_txion)
            self._storage.insert(current_txion.__repr__())
            self._chain_infos['txion_index'] += 1

        if 'message' in kwargs.keys():
            current_tlgrph = Telegraph(
                                  expeditor=kwargs['expeditor'],
                                  destinator=kwargs['destinator'],
                                  message=kwargs['message'],
                                  timestamp=datetime.datetime.now().strftime('%a, %d %b %Y %H:%M:%S'))

            self._cache_exchanges.append(current_tlgrph)
            self._chain_infos['telegraph_index'] += 1
            self._storage.insert(current_tlgrph.__repr__())

        self._save_chain_infos()
        return True

    def __repr__(self):
        return {'blockchain': self._storage.all()}

    def __str__(self):
        return self.__repr__().__str__()
