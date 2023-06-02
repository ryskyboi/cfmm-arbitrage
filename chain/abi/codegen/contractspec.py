import json
import os
from dataclasses import dataclass

from chain.abi.codegen.funcspec import FuncSpec
from chain.types import Address
from chain.contracts import ContractDefinition


@dataclass
class ContractSpec:
    name: str
    address: Address
    funcs: list[FuncSpec] = None

    @classmethod
    def from_json(cls, contract_def: ContractDefinition, abi_json: str) -> 'ContractSpec':
        func_dicts = json.loads(abi_json)
        funcs: list[FuncSpec] = []
        for func_dict in func_dicts:
            if func_dict["type"] != "function":
                continue
            func = FuncSpec.from_dict(func_dict)
            funcs.append(func)
        return ContractSpec(contract_def.name, contract_def.address, funcs)

    def generate_module_source(self) -> str:
        """
        Build ABI source code for contract class, extending BaseAbi, including supporting classes
        :return:
        """
        class_definitions = []
        module_header = """
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        """

        class_str = f"""
class {self.name}(BaseAbi):
    address: Address = Address("{self.address}")
"""
        for func in self.funcs:
            func_str = func.generate_method_source(class_definitions)
            # Indent func for use in class
            func_str = (os.linesep+"    ").join(func_str.split(os.linesep))
            class_str += "    "+func_str
        class_definitions.append(class_str)
        # Remove repeated class definitions
        unique_class_def = list(dict.fromkeys(class_definitions))
        return module_header+"".join(unique_class_def)
