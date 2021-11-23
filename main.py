
import time
from node import BlobNode


def forge_network():
    node_1 = BlobNode("127.0.0.1", 8001)
    node_2 = BlobNode("127.0.0.1", 8002)
    time.sleep(1)

    node_1.start()
    node_2.start()
    time.sleep(1)

    node_1.connect_with_node('127.0.0.1', 8002)
    node_2.connect_with_node('127.0.0.1', 8001)
    time.sleep(5)

    node_1.exchanges('txion', 'user1', 'user2', 10)
    time.sleep(10)
    node_1.forge()
    time.sleep(10)

    node_1.stop()
    node_2.stop()


def forge():
    node_1 = BlobNode("127.0.0.1", 8001)
    time.sleep(5)
    node_1.forge()
    time.sleep(5)
    node_1.stop()


def network():
    node_1 = BlobNode("127.0.0.1", 8001)
    node_2 = BlobNode("127.0.0.1", 8002)
    time.sleep(1)

    node_1.start()
    node_2.start()
    time.sleep(1)

    node_1.connect_with_node('127.0.0.1', 8002)
    node_2.connect_with_node('127.0.0.1', 8001)
    time.sleep(5)

    node_1.exchanges('txion', 'user1', 'user2', 10)
    time.sleep(10)

    node_1.stop()
    node_2.stop()


def initialise():
    node_1 = BlobNode("127.0.0.1", 8001)
    time.sleep(5)
    node_1.stop()


if __name__ == '__main__':
    initialise()
    time.sleep(15)

    network()
    time.sleep(15)

    forge()
    time.sleep(15)

    forge_network()
