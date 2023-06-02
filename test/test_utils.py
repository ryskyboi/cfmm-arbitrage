import json
from unittest import TestCase

from chain.abi.codegen.funcspec import FuncSpec
from chain.abi.codegen.varspec import VarSpec
from chain.api.dhv import DhvChainReader
from test import test_config

dhv = DhvChainReader.from_config(test_config())
abi = dhv.vol_feed.abi_json

print(abi)


# Tree = Union[tuple['Tree'], 'VarSpec']


class TestUtils(TestCase):
    def test_utils(self) -> None:
        funcs_json = [a for a in abi if a['type'] == "function"]

        my_json_str = json.dumps(funcs_json[0]["outputs"][0])
        v = VarSpec.from_json(my_json_str)
        func = FuncSpec.from_json(json.dumps(funcs_json[0]))
        funcs = [FuncSpec.from_json(json.dumps(f)) for f in funcs_json]
        for func in funcs:
            class_defs = []
            defn = func.generate_method_source(class_defs)
            for c in class_defs:
                print(c)
            print(defn)
            print("--------------")
        # for a in abi:
        #     if a['type'] == "function":
        #         print(a['name'], a['inputs'])
        #
