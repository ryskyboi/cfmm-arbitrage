from ast import literal_eval
from pathlib import Path
from typing import Any

from chain.types import Address, AbiJson
from chain.web3_api import Web3Endpoint

IS_ENABLE_WEB3_RECORDING = False
# IS_ENABLE_WEB3_RECORDING = True


def res_path() -> Path:
    return Path(__file__).parent / "res"


def res_file_path(address, func_name, arg_list) -> Path:
    arg_str = str(arg_list)
    if len(arg_str) > 128:
        from hashlib import md5
        arg_str = "#"+md5(arg_str.encode()).hexdigest()
    return res_path() / address / f"{func_name}{arg_str}.txt"


def save_res(address, func_name, arg_list, response) -> None:
    path = res_file_path(address, func_name, arg_list)
    path.parent.mkdir(exist_ok=True, parents=True)
    with open(path, "w") as fh:
        fh.write(repr(response))


def load_res(address, func_name, arg_list, is_just_text=False) -> Any:
    s: str
    with open(res_file_path(address, func_name, arg_list), "r") as fh:
        s = fh.read()
    return literal_eval(s) if not is_just_text else s


class MockW3E(Web3Endpoint):
    def __init__(self):
        ...

    def build_contract(self, *args):
        return None

    def call(self, address: Address, abi_json: AbiJson, func_name: str, **kwargs):
        return load_res(address, func_name, tuple(kwargs.values()))
