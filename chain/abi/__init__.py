import json
from pathlib import Path

import requests

from chain.chains import ChainDefinition
from chain.exceptions import ChainException
from chain.logger import log
from chain.types import AbiJson, Address


def download_abi(url: str, path: Path | str) -> None:
    log.debug(f"Downloading ABI {url} to {path}.")
    response = requests.get(url)
    scan_response = json.loads(response.content.decode())
    if not (scan_response["status"] == "1" and scan_response["message"] == "OK"):
        raise ChainException(f"Unable to download ABI: {url}. Got: {response.content}")
    abi_json = scan_response["result"]
    path.parent.mkdir(exist_ok=True, parents=True)
    with open(path, "w") as fh:
        fh.write(abi_json)


class AbiManager:
    def __init__(self, chain_def: ChainDefinition, abi_folder: str | Path):
        self._abi_folder = Path(abi_folder)
        self._chain_def = chain_def

    def abi_json_str(self, address: Address) -> str:
        abi_path = self._abi_folder / self._chain_def.name / address
        if not abi_path.exists():
            download_abi(self._chain_def.abi_url(address), abi_path)
        with open(abi_path) as fh:
            return fh.read()

    def abi_json(self, address: Address) -> AbiJson:
        return json.loads(self.abi_json_str(address))
