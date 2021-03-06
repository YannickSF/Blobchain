
import hashlib


class Block:
    def __init__(self, **kwargs):
        self.index = kwargs['index']
        self.data = kwargs['data']
        self.proof = kwargs['proof']
        self.timestamp = kwargs['timestamp']
        self.last_hash = kwargs['last_hash']
        self.forge_by = kwargs['forge_by']

        if 'hash' in kwargs.keys():
            self.hash = kwargs['hash']
        else:
            self._encode()

    def _encode(self):
        sha = hashlib.sha256()
        payload = {'index': '{0}'.format(self.index),
                   'data': '{0}'.format(self.data),
                   'proof': '{0}'.format(self.proof),
                   'timestamp': '{0}'.format(self.timestamp),
                   'last_hash': '{0}'.format(self.last_hash),
                   'forge_by': '{0}'.format(self.forge_by)}

        sha.update(str(payload).encode('utf-8'))
        self.hash = sha.hexdigest()

    def __repr__(self):
        return {'hash': self.hash,
                'index': self.index,
                'data': self.data,
                'proof': self.proof,
                'timestamp': self.timestamp,
                'last_hash': self.last_hash,
                'forge_by': self.forge_by}

    def __str__(self):
        return self.__repr__().__str__()
