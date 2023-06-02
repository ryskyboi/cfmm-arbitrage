from typing import Type, TypeVar

from chain.abi import AbiManager
from chain.abi.codegen import BaseAbi
from chain.abi.path import abi_resource_path
from chain.chains import ChainDefinition, CHAIN
from chain.config import Config
from chain.web3_api import Web3Endpoint

_Self = TypeVar("_Self", bound='ChainReader')

ContractAbi = TypeVar("ContractAbi", bound=BaseAbi)

class ChainReader:
    protocol_name: str

    def __init__(self, chain_def: ChainDefinition, web3_endpoint: Web3Endpoint, abi_manager: AbiManager):
        self._chain_def = chain_def
        self.web3_endpoint = web3_endpoint
        self.abi_manager = abi_manager

    @classmethod
    def from_config(cls: Type[_Self], config: Config) -> _Self:
        chain = CHAIN.find(config.chain_name)
        chain_def = chain.value
        return cls(
            chain_def,
            Web3Endpoint.from_config(config),
            AbiManager(chain_def, config.abi_resource_folder)
        )

    # TODO: tidy
    def _old_contract(self, contract_name: str) -> ContractAbi:
        import importlib
        contract_mod = importlib.import_module(f"chain.abi.{self._chain_def.name}.{self.protocol_name}.{contract_name}")
        contract_abi_cls: Type[ContractAbi] = getattr(contract_mod, contract_name)
        return contract_abi_cls(self.web3_endpoint, self.abi_manager)

    def _contract(self, contract_cls: Type[ContractAbi]) -> ContractAbi:
        return contract_cls(self.web3_endpoint, self.abi_manager)