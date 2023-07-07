from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, TypeVar

from chain.abi import AbiManager
from chain.abi.codegen.contractspec import ContractSpec
from chain.abi.codegen.protocolspec import ProtocolSpec
from chain.abi.path import abi_resource_path, abi_package_path
from chain.chains import CHAIN
from chain.contracts import ContractDefinition
from chain.logger import log
from chain.protocols import ProtocolDefinition
from chain.types import Address
from chain.web3_api import Web3Endpoint

IS_ENABLE_WEB3_RECORDING = False
try:
    from test.api.make_res import IS_ENABLE_WEB3_RECORDING as _
    IS_ENABLE_WEB3_RECORDING = _
except ModuleNotFoundError:
    pass

Self = TypeVar("Self")


class BaseAbi:
    address: Address

    def __init__(self, w3_endpoint: Web3Endpoint, abi_manager: AbiManager):
        self._w3_endpoint = w3_endpoint
        self.abi_manager = abi_manager

    def _call(self, func_name: str, **kwargs: Any):
        abi_json = self.abi_manager.abi_json(self.address)
        response = self._w3_endpoint.call(self.address, abi_json, func_name, **kwargs)
        if IS_ENABLE_WEB3_RECORDING:
            from test.api.make_res import save_res
            save_res(self.address, func_name, tuple(kwargs.values()), response)
        log.debug(str((self.__class__.__name__, func_name, tuple(kwargs.values()))))
        log.debug(response)
        return response


@dataclass
class AbiConfig:
    target_path_for_generated_code: str | Path = field(default_factory=abi_package_path)
    is_sync: bool = True
    is_async: bool = False

    def __post_init__(self):
        if self.target_path_for_generated_code:
            self.target_path_for_generated_code = Path(self.target_path_for_generated_code)
        else:
            self.target_path_for_generated_code = abi_resource_path()


class ProtocolAbiCodegen:
    """
    Python source code generation tool for any protocol's contracts for any supported chain.
    Produces a package for each chain,
    subpackage for per protocol
    module (python file) for each contract, extending BaseAbi
    eponymous class in said module for the contract
    method for each contract function
    """

    def __init__(self, config: AbiConfig, abi_manager: AbiManager, protocol_definition: ProtocolDefinition):
        self.config = config
        self.abi_manager = abi_manager
        self.protocol_definition = protocol_definition

    @classmethod
    def create(
            cls: type[Self],
            chain: CHAIN,
            protocol_name: str,
            contract_definitions: list[ContractDefinition]
    ) -> Self:
        return cls(
            AbiConfig(),
            AbiManager(chain.value, abi_resource_path()),
            ProtocolDefinition(
                protocol_name,
                chain,
                contract_definitions
            )
        )

    def generate_package_source(self, is_dry_run: bool = True) -> dict[Path, str]:
        """
        (Optionally) Write ABI python package source code files to target destination.
        :return: Map of filepath -> source code
        """
        log.debug(f"Generating for chain.abi.{self.protocol_definition.chain.name}.{self.protocol_definition.name}")
        protocol_spec = ProtocolSpec(self.protocol_definition, self.abi_manager)
        subpackage_source = protocol_spec.generate_subpackage_source()
        abi_path = self.config.target_path_for_generated_code
        chain_path = abi_path / self.protocol_definition.chain.name
        protocol_path = chain_path / self.protocol_definition.name
        package_source: dict[Path, str] = {}
        for sps_name, sps_code in subpackage_source.items():
            module = protocol_path / f"{sps_name}.py"
            package_source[module] = sps_code

        if not is_dry_run:
            def touch_init(folder_path: Path) -> None:
                folder_path.mkdir(exist_ok=True, parents=True)
                path_init = folder_path / "__init__.py"
                if not path_init.exists():
                    path_init.touch()

            touch_init(chain_path)
            touch_init(protocol_path)
            for path, source in package_source.items():
                with open(path, "w") as fh:
                    fh.write(source)

        return package_source
