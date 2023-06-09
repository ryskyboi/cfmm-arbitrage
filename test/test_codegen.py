from unittest import TestCase

from chain.abi.codegen.funcspec import FuncSpec
from chain.abi.codegen.varspec import VarSpec

my_json = """
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "name": "sabrParams",
    "outputs": [
      {
        "internalType": "int32",
        "name": "callAlpha",
        "type": "int32"
      },
      {
        "internalType": "int32",
        "name": "callBeta",
        "type": "int32"
      },
      {
        "internalType": "int32",
        "name": "callRho",
        "type": "int32"
      },
      {
        "internalType": "int32",
        "name": "callVolvol",
        "type": "int32"
      },
      {
        "internalType": "int32",
        "name": "putAlpha",
        "type": "int32"
      },
      {
        "internalType": "int32",
        "name": "putBeta",
        "type": "int32"
      },
      {
        "internalType": "int32",
        "name": "putRho",
        "type": "int32"
      },
      {
        "internalType": "int32",
        "name": "putVolvol",
        "type": "int32"
      },
      {
        "internalType": "int256",
        "name": "interestRate",
        "type": "int256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }"""

component_varspc_json_str = """
      {
        "components": [
          {
            "internalType": "int32",
            "name": "callAlpha",
            "type": "int32"
          }
        ],
        "internalType": "struct VolatilityFeed.SABRParams",
        "name": "_sabrParams",
        "type": "tuple"
      }
"""

set_sabr_funcspec_json_str = """
  {
    "inputs": [
      {
        "components": [
          {
            "internalType": "int32",
            "name": "callAlpha",
            "type": "int32"
          },
          {
            "internalType": "int32",
            "name": "callBeta",
            "type": "int32"
          },
          {
            "internalType": "int32",
            "name": "callRho",
            "type": "int32"
          },
          {
            "internalType": "int32",
            "name": "callVolvol",
            "type": "int32"
          },
          {
            "internalType": "int32",
            "name": "putAlpha",
            "type": "int32"
          },
          {
            "internalType": "int32",
            "name": "putBeta",
            "type": "int32"
          },
          {
            "internalType": "int32",
            "name": "putRho",
            "type": "int32"
          },
          {
            "internalType": "int32",
            "name": "putVolvol",
            "type": "int32"
          },
          {
            "internalType": "int256",
            "name": "interestRate",
            "type": "int256"
          }
        ],
        "internalType": "struct VolatilityFeed.SABRParams",
        "name": "_sabrParams",
        "type": "tuple"
      },
      {
        "internalType": "uint256",
        "name": "_expiry",
        "type": "uint256"
      }
    ],
    "name": "setSabrParameters",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
"""
def my_dict():
    return {
        'inputs': [
            VarSpec(
                internal_type='struct VolatilityFeed.SABRParams',
                name='_sabrParams',
                type='tuple',
                components=[
                    VarSpec(internal_type='int32', name='callAlpha', type='int32', components=[]),
                    VarSpec(internal_type='int32', name='callBeta', type='int32', components=[]),
                    VarSpec(internal_type='int32', name='callRho', type='int32', components=[]),
                    VarSpec(internal_type='int32', name='callVolvol', type='int32', components=[]),
                    VarSpec(internal_type='int32', name='putAlpha', type='int32', components=[]),
                    VarSpec(internal_type='int32', name='putBeta', type='int32', components=[]),
                    VarSpec(internal_type='int32', name='putRho', type='int32', components=[]),
                    VarSpec(internal_type='int32', name='putVolvol', type='int32', components=[]),
                    VarSpec(internal_type='int256', name='interestRate', type='int256', components=[])
                ]
            ),
            VarSpec(internal_type='uint256', name='_expiry', type='uint256', components=[])
        ],
        'name': 'setSabrParameters',
        'outputs': [],
        'state_mutability': 'nonpayable',
        'type': 'function'
    }


class TestFuncSpec(TestCase):
    def test_funcspec(self) -> None:
        FuncSpec.from_json(my_json)

    def test_varspec_component(self) -> None:
        VarSpec.from_json(component_varspc_json_str)

    def test_funcspec_set_sabr(self) -> None:
        fs = FuncSpec.from_json(set_sabr_funcspec_json_str)
        # TODO: make into a proper unit test
        print(fs)
