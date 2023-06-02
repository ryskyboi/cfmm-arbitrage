from pathlib import Path


def abi_resource_path():
    return Path(__file__).parent / "res"


def abi_package_path():
    return Path(__file__).parent
