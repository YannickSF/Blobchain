
import hashlib


class Txion:
    def __init__(self, **kwargs):
        self.expeditor = kwargs['expeditor']
        self.destinator = kwargs['destinator']
        self.amount = kwargs['amount']
        self.timestamp = kwargs['timestamp']
        self.nounce = kwargs['nounce']
        self.index = kwargs['index']

        if 'hash' in kwargs.keys():
            self.hash = kwargs['hash']
        else:
            self._encode()

    def _encode(self):
        sha = hashlib.sha256()
        payload = {
            'expeditor': self.expeditor,
            'destinator': self.destinator,
            'amount': self.amount,
            'timestamp': self.timestamp,
            'nounce': self.nounce,
            'index': self.index
        }

        sha.update(str(payload).encode('utf-8'))
        self.hash = sha.hexdigest()

    def __repr__(self):
        return {'expeditor': self.expeditor,
                'destinator': self.destinator,
                'amount': self.amount,
                'timestamp': self.timestamp,
                'nounce': self.nounce,
                'hash': self.hash,
                'index': self.index}

    def __str__(self):
        return self.__repr__().__str__()
