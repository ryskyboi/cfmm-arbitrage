from ast import literal_eval
from pathlib import Path
from typing import Any

from chain.types import Address, AbiJson
from chain.web3_api import Web3Endpoint

IS_ENABLE_WEB3_RECORDING = False
# IS_ENABLE_WEB3_RECORDING = True


def res_file_path(protocol: str, address, func_name, arg_list) -> Path:
    arg_str = str(arg_list)
    if len(arg_str) > 128:
        from hashlib import md5
        arg_str = "#"+md5(arg_str.encode()).hexdigest()
    return Path(__file__).parent / protocol / "res" / address / f"{func_name}{arg_str}.txt"


def save_res(protocol: str, address, func_name, arg_list, response) -> None:
    path = res_file_path(protocol, address, func_name, arg_list)
    path.parent.mkdir(exist_ok=True, parents=True)
    with open(path, "w") as fh:
        fh.write(repr(response))


def load_res(protocol: str, address, func_name, arg_list, is_just_text=False) -> Any:
    s: str
    with open(res_file_path(protocol, address, func_name, arg_list), "r") as fh:
        s = fh.read()
    return literal_eval(s) if not is_just_text else s


class MockW3E(Web3Endpoint):
    # Since we mock out all functionality, we deliberately do not call super initialiser.
    # noinspection PyMissingConstructor
    def __init__(self, protocol_name: str):
        self._protocol_name = protocol_name
        ...

    def build_contract(self, *args):
        return None

    def call(self, address: Address, abi_json: AbiJson, func_name: str, **kwargs):
        return load_res(self._protocol_name, address, func_name, tuple(kwargs.values()))
