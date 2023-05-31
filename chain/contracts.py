import web3.contract as wc


class Contract:
    def __init__(self, web3_contract: wc.Contract, abi_json: dict):
        self._w3_contract = web3_contract
        self._abi_json = abi_json

    @property
    def abi_json(self) -> dict:
        return self._abi_json
