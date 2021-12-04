
from core.settings import SETTINGS
from p2pnetwork.node import Node
from core.blockchain import Blockchain


class BlobNode(Node):
    def __init__(self, host, port, callback=None, max_connections=0):
        super(BlobNode, self).__init__(host, port, None, callback, max_connections)
        self._blockchain = Blockchain()
        print("Node {} - port {}: Started".format(self.id, port))

    def blocks(self, *args):
        if len(args) > 0:
            return self._blockchain.block(args[0])
        else:
            return self._blockchain.__repr__()

    def exchanges(self, b_type, exp, to, value):
        payload = {'b_type': b_type}
        ex_callback = None

        if b_type == 'txion':
            new_txion = self._blockchain.exchanges(exp, to, value)
            payload['item'] = new_txion.__repr__()
            ex_callback = new_txion

        self.send_to_nodes(payload)
        return ex_callback

    def forge(self):
        new_block = self._blockchain.forge()
        payload = {'b_type': 'block', 'item': new_block.__repr__()}
        self.send_to_nodes(data=payload)
        return new_block

    # all the methods below are called when things happen in the network.
    # implement your network node behavior to create the required functionality.

    def outbound_node_connected(self, node):
        # this connect to other
        print("outbound_node_connected (" + self.id + "): " + node.id)

    def inbound_node_connected(self, node):
        # other connect to this
        payload = self.blocks()
        payload['synchronisation'] = True
        self.send_to_node(node, payload)
        print("inbound_node_connected: (" + self.id + "): " + node.id)

    def outbound_node_disconnected(self, node):
        print("outbound_node_disconnected: (" + self.id + "): " + node.id)

    def inbound_node_disconnected(self, node):
        print("inbound_node_disconnected: (" + self.id + "): " + node.id)

    def node_message(self, node, data):
        print("node_message (" + self.id + ") from " + node.id + ": " + str(data))
        if 'synchronisation' in data.keys():
            synchronisation_state, synchronisation_chain = self._blockchain.synchronise(data['synchronisation'],
                                                                                        blockchain=data['blockchain'])
            if not synchronisation_state:
                self.send_to_node(node, {'synchronisation_resolve': True, 'resolve_chain': synchronisation_chain})
        elif 'b_type' in data.keys():
            self._blockchain.peers_exchanges(data['b_type'], data['item'])
        else:
            self._blockchain.peers_exchanges(None, data)

    def node_request_to_stop(self):
        print("node is requested to stop (" + self.id + "): ")


if __name__ == '__main__':
    n = BlobNode(SETTINGS.HOST, SETTINGS.PORT)
    n.start()

    stop = False
    while not stop:
        outbound = input('Press \'0\' to stop. \n')
        if int(outbound) == 0:
            stop = True

    if stop:
        n.stop()

