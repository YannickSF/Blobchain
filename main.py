
import time
from node import BlobNode


def network():
    node_1 = BlobNode("127.0.0.1", 8001)
    node_2 = BlobNode("127.0.0.1", 8002)
    node_3 = BlobNode("127.0.0.1", 8003)

    time.sleep(1)

    node_1.start()
    node_2.start()
    node_3.start()

    time.sleep(1)

    node_1.connect_with_node('127.0.0.1', 8002)
    node_2.connect_with_node('127.0.0.1', 8003)
    node_3.connect_with_node('127.0.0.1', 8001)

    time.sleep(5)

    node_1.exchanges('user1', 'user2', 10)

    time.sleep(30)

    node_1.stop()
    node_2.stop()
    node_3.stop()
    print('end test')


def initialise():
    node_1 = BlobNode("127.0.0.1", 8001)
    time.sleep(5)
    node_1.stop()


if __name__ == '__main__':
    initialise()
