
import random
import hashlib
from core.settings import SETTINGS

WORDS_BANK = ['Composé', 'Cactus', 'Madrid', 'Câbles', 'Câblage', 'Pause', 'Ronflement', 'Carburant', 'Décoration',
              'Chômage', 'Laitue', 'Infraction', 'Paille', 'Kiosque', 'Tortue', 'Invisible', 'Drôle', 'Quartier',
              'Archive', 'Électricité', 'Canard', 'Tension', 'Conjoint', 'Falaise', 'Sauce']


def get_secret_phrases():
    return ' '.join([random.choice(WORDS_BANK) for i in range(12)])


class Wallet:
    def __init__(self):
        self._secret_phrase = None
        self._private_key = None
        self.public_key = None

    def create(self, password):
        cuter_private = hashlib.sha256()
        self._secret_phrase = get_secret_phrases()
        cuter_private.update(bytes('{}-WALLET_USAGE'.format(SETTINGS.NAME).encode()))
        cuter_private.update(bytes('{}'.format(self._secret_phrase).encode()))
        cuter_private.update(bytes('{}'.format(password).encode()))
        cuter_private.update(bytes('{}'.format(SETTINGS.SIGNATURE).encode()))
        self._private_key = cuter_private.hexdigest()

        cuter_public = hashlib.sha256()
        cuter_public.update(bytes('{}'.format(self._secret_phrase).encode()))
        cuter_public.update(bytes('{}'.format(password).encode()))
        self.public_key = cuter_public.hexdigest()

    def open(self, private_key, password, secret_phrase):
        cuter_private = hashlib.sha256()
        cuter_private.update(bytes('{}-WALLET_USAGE'.format(SETTINGS.NAME).encode()))
        cuter_private.update(bytes('{}'.format(secret_phrase).encode()))
        cuter_private.update(bytes('{}'.format(password).encode()))
        cuter_private.update(bytes('{}'.format(SETTINGS.SIGNATURE).encode()))

        guessing_private = cuter_private.hexdigest()
        if private_key == guessing_private:
            self._secret_phrase = secret_phrase
            self._private_key = guessing_private

            cuter_public = hashlib.sha256()
            cuter_public.update(bytes('{}'.format(secret_phrase).encode()))
            cuter_public.update(bytes('{}'.format(password).encode()))
            self.public_key = cuter_public.hexdigest()

    def __repr__(self):
        return {
            'secret_phrase': self._secret_phrase,
            'private_key': self._private_key,
            'public_key': self.public_key
        }

    def __str__(self):
        return self.__repr__().__str__()


if __name__ == '__main__':
    print('------- CREATE BLOB_CHAIN WALLET -------')
    w = Wallet()
    w.create(input('Enter password : \n'))
    print('------- DONE -------')
    print((w.__str__()))
    print('------- /GOLDEN_BLOB\\ -------')

