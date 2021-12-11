
import time
from core.settings import SETTINGS
from node import BlobNode
from core.wallet import Wallet


def client():

    def find_block():
        print('-------------------- BLOB_CHAIN CLIENT --------------------')
        print('-------------------- BLOCK SEARCH --------------------')
        value = input('Enter hash : \n')
        print(n.blocks(value))

    def connect_outbound():
        print('-------------------- BLOB_CHAIN CLIENT --------------------')
        print('-------------------- CONNECT --------------------')
        value = input('Enter outbound_node host : \n')
        # check format
        print('ADD : {} - ASK'.format(value))
        n.connect_with_node(value, SETTINGS.PORT)
        print('ADD : {} - DONE'.format(value))

    def exchange():
        print('-------------------- BLOB_CHAIN CLIENT --------------------')
        print('-------------------- EXCHANGE --------------------')
        expeditor = input('From : \n')
        destinator = input('To : \n')
        amount = input('Amount : \n')
        print(n.exchanges('txion', expeditor, destinator, amount))

    def forge():
        print('-------------------- BLOB_CHAIN CLIENT --------------------')
        print('-------------------- FORGE --------------------')
        print(n.forge())

    def wallet():

        def create_wallet():
            print('-------------------- WALLET --------------------')
            print('-------------------- CREATE --------------------')
            password = input('Enter password : \n')
            print('generating secret_phrase')
            new_wallet = Wallet()
            new_wallet.create(password)
            print('generating wallet')
            print(new_wallet.__repr__())
            print('Keep private_key, password & secret_phrase secret !')
            print('-------------------- Exit : 0 --------------------')

        def open_wallet():
            print('-------------------- WALLET --------------------')
            print('-------------------- CONNECT --------------------')
            private_key = input('Enter private_key : \n')
            password = input('Enter password : \n')
            secret_phrase = input('Enter secret_phrase : \n')
            current_wallet = Wallet()
            current_wallet.open(private_key, password, secret_phrase)
            print(current_wallet.__repr__())
            print('-------------------- Exit Wallet : 0 --------------------')

        stop_wallet = False
        while not stop_wallet:
            print('-------------------- BLOB_CHAIN CLIENT --------------------')
            print('-------------------- WALLET --------------------')
            print('1. create')
            print('2. connect')
            print('0. exit -> exit Wallet')
            option_wallet = input('Choose option : \n')

            if int(option_wallet) == 0:
                stop_wallet = True
            elif int(option_wallet) == 1:
                create_wallet()
            elif int(option_wallet) == 2:
                open_wallet()

    print('Initialise client... ')
    n = BlobNode(SETTINGS.HOST, SETTINGS.PORT)
    n.start()
    time.sleep(1)
    print('- BLOB_NODE Started ! ')

    stop = False
    while not stop:
        print('-------------------- BLOB_CHAIN CLIENT --------------------')
        print('1. Find_block')
        print('2. Connect to node')
        print('3. Exchange')
        print('4. Forge')
        print('5. Wallet >>')
        print('0. exit -> stop Node')
        option = input('Choose option : \n')

        if int(option) == 0:
            stop = True
        elif int(option) == 1:
            find_block()
        elif int(option) == 2:
            connect_outbound()
        elif int(option) == 3:
            exchange()
        elif int(option) == 4:
            forge()
        elif int(option) == 5:
            wallet()
        else:
            print(option)

    if stop:
        n.stop()


if __name__ == '__main__':
    client()
