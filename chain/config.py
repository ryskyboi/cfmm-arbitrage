from dataclasses import dataclass, field
from chain.abi.path import abi_resource_path


@dataclass
class Config:
    alchemy_key: str
    chain_name: str
    abi_resource_folder: str = field(default_factory=abi_resource_path)
