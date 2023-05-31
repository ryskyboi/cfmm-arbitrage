import json
from pathlib import Path

import requests

from chain.chains import ChainDefinition
from chain.exceptions import ChainException
from chain.logger import log


class AbiJson(dict):
    ...


def download_abi(url: str, path: Path | str) -> None:
    log.debug(f"Downloading ABI {url} to {path}.")
    response = requests.get(url)
    scan_response = json.loads(response.content.decode())
    if not (scan_response["status"] == "1" and scan_response["message"] == "OK"):
        raise ChainException(f"Unable to download ABI: {url}. Got: {response.content}")
    abi_json = scan_response["result"]
    with open(path, "w") as fh:
        fh.write(abi_json)


def abi_resource_path():
    return Path(__file__).parent / "res"


class AbiManager:
    def __init__(self, chain_def: ChainDefinition, abi_folder: str | Path):
        self._abi_folder = Path(abi_folder)
        self._chain_def = chain_def

    def abi_json(self, address: str) -> AbiJson:
        abi_path = self._abi_folder / self._chain_def.name / address
        if not abi_path.exists():
            download_abi(self._chain_def.abi_url(address), abi_path)
        with open(abi_path) as fh:
            return json.loads(fh.read())
