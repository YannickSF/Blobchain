
import hashlib


class Block:
    def __init__(self, index=None, data=None, timestamp=None, last_hash=None, serial=False, hash=None):
        self.index = index
        self.data = data
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = None

        if serial is False:
            self._bc_format()
        else:
            self.hash = hash

    def _bc_format(self):
        sha = hashlib.sha256()
        payload = {'index': '{0}'.format(self.index),
                   'data': '{0}'.format(self.data),
                   'timestamp': '{0}'.format(self.timestamp),
                   'last_hash': '{0}'.format(self.last_hash)}

        sha.update(str(payload).encode('utf-8'))

        self.hash = sha.hexdigest()

    def __repr__(self):
        return {'hash': self.hash,
                'index': self.index,
                'data': self.data,
                'timestamp': self.timestamp,
                'last_hash': self.last_hash}

    def __str__(self):
        return self.__repr__().__str__()


class Txion:
    def __init__(self, index, expeditor, destinator, amount, timestamp, nounce=None, phash=None):
        self.index = index
        self.expeditor = expeditor
        self.destinator = destinator
        self.amount = amount
        self.timestamp = timestamp
        self.nounce = nounce
        self.hash = phash

    def _bc_format(self):
        sha = hashlib.sha256()
        payload = {'index': self.index,
                   'expeditor': self.expeditor,
                   'destinator': self.destinator,
                   'amount': self.amount,
                   'timestamp': self.timestamp,
                   'nounce': self.nounce,
                   'hash': self.hash}

        sha.update(str(payload).encode('utf-8'))

        self.hash = sha.hexdigest()

    def __repr__(self):
        return {'index': self.index,
                'expeditor': self.expeditor,
                'destinator': self.destinator,
                'amount': self.amount,
                'timestamp': self.timestamp,
                'nounce': self.nounce,
                'hash': self.hash}

    def __str__(self):
        return self.__repr__().__str__()


class Telegraph:
    def __init__(self, expeditor, destinator, message, timestamp, serial=False, hash=''):
        self.expeditor = expeditor
        self.destinator = destinator
        self.message = message
        self.timestamp = timestamp
        self.hash = None

        if serial is False:
            self._bc_format()
        else:
            self.hash = hash

    def _bc_format(self):
        sha = hashlib.sha256()
        payload = {'expeditor': self.expeditor,
                   'destinator': self.destinator,
                   'message': self.message,
                   'timestamp': self.timestamp,
                   'hash': self.hash}

        sha.update(str(payload).encode('utf-8'))

        self.hash = sha.hexdigest()

    def __repr__(self):
        return {'hash': self.hash,
                'expeditor': self.expeditor,
                'destinator': self.destinator,
                'message': self.message,
                'timestamp': self.timestamp}

    def __str__(self):
        return self.__repr__().__str__()
