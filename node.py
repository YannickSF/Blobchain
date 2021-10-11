
from core.settings import SETTINGS
from core.network import Network
from core.blockchain import Blockchain


class BlobNode:
	def __init__(self, host=SETTINGS.HOST, port=SETTINGS.PORT, id=0):
		self.blockchain = Blockchain()
		self.network = Network(host=host, port=port, blockchain=self.blockchain, id=id)

	def block(self, *args):
		if len(args) > 0:
			return self.blockchain.block(args[0])
		else:
			return self.blockchain.__repr__()

	def synchronise(self):
		pass

	def exchanges(self, exp, dest, value):
		new_txion = self.blockchain.exchanges(exp, dest, value)
		self.network.send_to_nodes(new_txion.__repr__())

	def forge(self):
		pass

	def stop(self):
		self.network.stop()


if __name__ == "__main__":
	n = BlobNode()
	print(n.block('hash'))
	n.stop()
