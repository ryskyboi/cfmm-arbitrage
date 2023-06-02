from enum import Enum

from chain.exceptions import ChainException


class ChainDefinition:
    def __init__(self, name: str, alchemy_url_stub: str, scan_io_abi_url_stub: str):
        self.name = name
        self._alchemy_url_stub = alchemy_url_stub
        self._scan_io_abi_url_stub = scan_io_abi_url_stub

    def alchemy_url(self, key: str) -> str:
        return self._alchemy_url_stub + key

    def abi_url(self, address: str):
        return self._scan_io_abi_url_stub + address


class CHAIN(Enum):
    @staticmethod
    def find(chain_name: str) -> 'CHAIN':
        for chain in CHAIN:
            if chain.name == chain_name:
                return chain
        raise ChainException(f"Cannot find chain with name {chain_name} in CHAINS.")

    ARBITRUM_GOERLI = ChainDefinition(
        "ARBITRUM_GOERLI",
        "https://arb-goerli.g.alchemy.com/v2/",
        "https://api-goerli.arbiscan.io/api?module=contract&action=getabi&address=",
    )
