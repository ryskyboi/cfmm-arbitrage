from typing import Type, TypeVar

from web3.contract import Contract

from chain.chains import ChainDefinition, CHAIN
from chain.config import Config
from chain.web3_api import Web3Endpoint

_Self = TypeVar("_Self", bound='ChainReader')


class ChainReader:
    def __init__(self, chain_def: ChainDefinition, web3_endpoint: Web3Endpoint):
        self._chain_def = chain_def
        self.web3_endpoint = web3_endpoint

    @classmethod
    def from_config(cls: Type[_Self], config: Config) -> _Self:
        chain = CHAIN.find(config.chain_name)
        chain_def = chain.value
        return cls(
            chain_def,
            Web3Endpoint.from_config(config)
        )
