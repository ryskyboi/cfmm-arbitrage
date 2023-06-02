from typing import TypeVar, Type

import web3
import web3.contract

from chain.abi import AbiManager
from chain.types import AbiJson, Address
from chain.chains import CHAIN
from chain.chains.address_register import AddressManager
from chain.config import Config
from chain.contracts import Contract
from chain.protocols import ContractName


class Web3Endpoint:
    def __init__(self, w3: web3.Web3, abi_manager: AbiManager, address_manager: AddressManager):
        self.w3 = w3
        self._abi_manager = abi_manager
        self._address_manager = address_manager

    @classmethod
    def from_config(cls, config: Config):
        chain = CHAIN.find(config.chain_name)
        chain_def = chain.value
        return Web3Endpoint(
            web3.Web3(
                web3.Web3.HTTPProvider(
                    chain_def.alchemy_url(config.alchemy_key)
                )
            ),
            AbiManager(chain_def, config.abi_resource_folder),
            AddressManager(chain)
        )

    def _abi_json(self, address: Address) -> AbiJson:
        return self._abi_manager.abi_json(address)

    ContractClass = TypeVar("ContractClass", bound=Contract)

    def build_contract(self, contract_name: ContractName, contract_class: Type[ContractClass]) -> ContractClass:
        address: Address = self._address_manager.address(contract_name)
        abi = self._abi_json(address)

        # Correct web3 statement follows, but its type hints bug out.
        # noinspection PyTypeChecker
        w3_contract = self.w3.eth.contract(address, abi=abi)

        return contract_class(w3_contract, abi)

    def call(self, address: Address, abi_json: AbiJson, func_name: str, **kwargs):
        """Call the function on the contract, with optional kwargs. You must be on the correct chain!"""
        w3_contract = self.w3.eth.contract(address, abi=abi_json)
        result = w3_contract.functions[func_name](*kwargs.values()).call()
        return result
