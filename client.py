
import time
from core.settings import SETTINGS
from node import BlobNode
from core.wallet import Wallet


class Client:
    def __init__(self):
        print('Initialise client... ')
        self.client_node = BlobNode(SETTINGS.HOST, SETTINGS.PORT)
        self.client_node.start()
        time.sleep(1)
        print('- BLOB_NODE Started ! ')

        self.connected_wallet = Wallet()

    def find_block(self):
        print('-------------------- BLOB_CHAIN CLIENT --------------------')
        print('-------------------- BLOCK SEARCH --------------------')
        value = input('Enter hash : \n')
        print(self.client_node.blocks(value))

    def connect_outbound(self):
        print('-------------------- BLOB_CHAIN CLIENT --------------------')
        print('-------------------- CONNECT --------------------')
        value = input('Enter outbound_node host : \n')
        # check format
        print('ADD : {} - ASK'.format(value))
        self.client_node.connect_with_node(value, SETTINGS.PORT)
        print('ADD : {} - DONE'.format(value))

    def exchange(self):
        print('-------------------- BLOB_CHAIN CLIENT --------------------')
        print('-------------------- EXCHANGE --------------------')
        expeditor = input('From : \n')
        destinator = input('To : \n')
        amount = input('Amount : \n')
        print(self.client_node.exchanges('txion', expeditor, destinator, amount))

    def forge(self):
        print('-------------------- BLOB_CHAIN CLIENT --------------------')
        print('-------------------- FORGE --------------------')
        print(self.client_node.forge(self.connected_wallet.public_key))

    def wallet(self):
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
            self.connected_wallet.open(private_key, password, secret_phrase)
            print(self.connected_wallet.__repr__())
            print('-------------------- Exit Wallet : 0 --------------------')

        def balance():
            print('-------------------- WALLET --------------------')
            print('-------------------- CONNECT --------------------')
            print(str(self.client_node.balance(self.connected_wallet.public_key)) + ' Tokens')
            print('-------------------- Exit Wallet : 0 --------------------')

        stop_wallet = False
        while not stop_wallet:
            print('-------------------- BLOB_CHAIN CLIENT --------------------')
            if self.connected_wallet.public_key is not None:
                print('key ' + self.connected_wallet.public_key)
            print('-------------------- WALLET --------------------')
            print('1. create')
            print('2. connect')
            print('3. balance')
            print('0. exit -> exit Wallet')
            option_wallet = input('Choose option : \n')

            if int(option_wallet) == 0:
                stop_wallet = True
            elif int(option_wallet) == 1:
                create_wallet()
            elif int(option_wallet) == 2:
                open_wallet()
            elif int(option_wallet) == 3:
                balance()

    def start(self):
        stop = False
        while not stop:
            print('\n')
            print('-------------------- BLOB_CHAIN CLIENT --------------------')
            if self.connected_wallet.public_key is not None:
                print('key ' + self.connected_wallet.public_key)
            print('------------------------------------------------------------')
            print('1. Find_block')
            print('2. Connect to node')
            print('3. Exchange')
            print('4. Forge')
            print('5. >|Wallet')
            print('0. >|Exit Node')
            option = input('Choose option : \n')

            if int(option) == 0:
                stop = True
            elif int(option) == 1:
                self.find_block()
            elif int(option) == 2:
                self.connect_outbound()
            elif int(option) == 3:
                self.exchange()
            elif int(option) == 4:
                self.forge()
            elif int(option) == 5:
                self.wallet()
            else:
                print(option)

        if stop:
            self.client_node.stop()


if __name__ == '__main__':
    cli = Client()
    cli.start()
