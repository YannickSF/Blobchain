
class _TestNetSettings:
    # BLOCKCHAIN
    NAME = '-BLOB_CHAIN-'
    SIGNATURE = 'origin-319838453e0be92c89f3cf3c26849418bae38a36d6f46942e908b49216affaf6'
    COIN_NAME = '-GOLDEN_BLOB-'
    COIN = 1000000000
    REWARD_MIN = 2
    REWARD_MAX = 20

    # NETWORK
    HOST = '0.0.0.0'
    PORT = 7702

    NETWORK = 'test'
    NETWORK_PATH = 'network'


class _MainNetSettings:
    # BLOCKCHAIN
    NAME = '-BLOB_CHAIN-'
    SIGNATURE = ''
    COIN_NAME = '-GOLDEN_BLOB-'
    COIN = 1000000000
    REWARD_MIN = 1
    REWARD_MAX = 10

    # NETWORK
    HOST = '0.0.0.0'
    PORT = 7701

    NETWORK = 'main'
    NETWORK_PATH = 'network'


SETTINGS = _TestNetSettings()
