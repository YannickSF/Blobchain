
import time
from node import BlobNode


if __name__ == '__main__':
    node_1 = BlobNode("127.0.0.1", 8001, id=1)
    node_2 = BlobNode("127.0.0.1", 8002, id=2)
    node_3 = BlobNode("127.0.0.1", 8003, id=3)

    time.sleep(1)

    node_1.network.start()
    node_2.network.start()
    node_3.network.start()

    time.sleep(1)

    node_1.network.connect_with_node('127.0.0.1', 8002)
    node_2.network.connect_with_node('127.0.0.1', 8003)
    node_3.network.connect_with_node('127.0.0.1', 8001)

    time.sleep(5)

    node_1.exchanges('user1', 'user2', 10)

    time.sleep(30)

    node_1.stop()
    node_2.stop()
    node_3.stop()
    print('end test')
