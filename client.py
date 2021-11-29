
import time
from core.settings import SETTINGS
from node import BlobNode


def client():

    def find_block():
        value = input('Enter hash : \n')
        print(n.blocks(value))

    def connect_outbound():
        value = input('Enter outbound_node host : \n')
        # check format
        print('ADD : {} - ASK'.format(value))
        n.connect_with_node(value, SETTINGS.PORT)
        print('ADD : {} - DONE'.format(value))

    def exchange():
        expeditor = input('From : \n')
        destinator = input('To : \n')
        amount = input('Amount : \n')
        print(n.exchanges('txion', expeditor, destinator, amount))

    def forge():
        print(n.forge())

    print('- BLOB_CHAIN CLIENT - ')
    print('Initialise... ')
    n = BlobNode(SETTINGS.HOST, SETTINGS.PORT)
    n.start()
    time.sleep(1)
    print('- BLOB_NODE Started ! ')

    stop = False
    while not stop:
        print('--------------------------------------')
        print('1. find_block')
        print('2. connect to node')
        print('3. exchange')
        print('4. forge')
        print('0. exit -> will stop node')
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
        else:
            print(option)

    if stop:
        n.stop()


if __name__ == '__main__':
    client()
