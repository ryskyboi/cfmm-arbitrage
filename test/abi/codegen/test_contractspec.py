from unittest import TestCase

from chain.abi.codegen.contractspec import ContractSpec
from chain.types import Address
from chain.contracts import ContractDefinition

abi_json = """
[
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "_authority",
        "type": "address"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "inputs": [],
    "name": "AlphaError",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "BetaError",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "IVNotFound",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "InterestRateError",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "NotKeeper",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "OptionExpiryInvalid",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "PRBMathSD59x18__AbsInputTooSmall",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "PRBMathSD59x18__DivInputTooSmall",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "rAbs",
        "type": "uint256"
      }
    ],
    "name": "PRBMathSD59x18__DivOverflow",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "int256",
        "name": "x",
        "type": "int256"
      }
    ],
    "name": "PRBMathSD59x18__Exp2InputTooBig",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "int256",
        "name": "x",
        "type": "int256"
      }
    ],
    "name": "PRBMathSD59x18__ExpInputTooBig",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "int256",
        "name": "x",
        "type": "int256"
      }
    ],
    "name": "PRBMathSD59x18__LogInputTooSmall",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "PRBMathSD59x18__MulInputTooSmall",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "rAbs",
        "type": "uint256"
      }
    ],
    "name": "PRBMathSD59x18__MulOverflow",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "rAbs",
        "type": "uint256"
      }
    ],
    "name": "PRBMathSD59x18__PowuOverflow",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "int256",
        "name": "x",
        "type": "int256"
      }
    ],
    "name": "PRBMathSD59x18__SqrtNegativeInput",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "int256",
        "name": "x",
        "type": "int256"
      }
    ],
    "name": "PRBMathSD59x18__SqrtOverflow",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "prod1",
        "type": "uint256"
      }
    ],
    "name": "PRBMath__MulDivFixedPointOverflow",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "prod1",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "denominator",
        "type": "uint256"
      }
    ],
    "name": "PRBMath__MulDivOverflow",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "RhoError",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "UNAUTHORIZED",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "VolvolError",
    "type": "error"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": false,
        "internalType": "contract IAuthority",
        "name": "authority",
        "type": "address"
      }
    ],
    "name": "AuthorityUpdated",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": false,
        "internalType": "address",
        "name": "keeper",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "bool",
        "name": "auth",
        "type": "bool"
      }
    ],
    "name": "KeeperUpdated",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "_expiry",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "int32",
        "name": "callAlpha",
        "type": "int32"
      },
      {
        "indexed": false,
        "internalType": "int32",
        "name": "callBeta",
        "type": "int32"
      },
      {
        "indexed": false,
        "internalType": "int32",
        "name": "callRho",
        "type": "int32"
      },
      {
        "indexed": false,
        "internalType": "int32",
        "name": "callVolvol",
        "type": "int32"
      },
      {
        "indexed": false,
        "internalType": "int32",
        "name": "putAlpha",
        "type": "int32"
      },
      {
        "indexed": false,
        "internalType": "int32",
        "name": "putBeta",
        "type": "int32"
      },
      {
        "indexed": false,
        "internalType": "int32",
        "name": "putRho",
        "type": "int32"
      },
      {
        "indexed": false,
        "internalType": "int32",
        "name": "putVolvol",
        "type": "int32"
      },
      {
        "indexed": false,
        "internalType": "int256",
        "name": "interestRate",
        "type": "int256"
      }
    ],
    "name": "SabrParamsSet",
    "type": "event"
  },
  {
    "inputs": [],
    "name": "authority",
    "outputs": [
      {
        "internalType": "contract IAuthority",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "name": "expiries",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getExpiries",
    "outputs": [
      {
        "internalType": "uint256[]",
        "name": "",
        "type": "uint256[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bool",
        "name": "isPut",
        "type": "bool"
      },
      {
        "internalType": "uint256",
        "name": "underlyingPrice",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "strikePrice",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "expiration",
        "type": "uint256"
      }
    ],
    "name": "getImpliedVolatility",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "vol",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bool",
        "name": "isPut",
        "type": "bool"
      },
      {
        "internalType": "uint256",
        "name": "underlyingPrice",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "strikePrice",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "expiration",
        "type": "uint256"
      }
    ],
    "name": "getImpliedVolatilityWithForward",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "vol",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "forward",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "name": "keeper",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
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
  },
  {
    "inputs": [
      {
        "internalType": "contract IAuthority",
        "name": "_newAuthority",
        "type": "address"
      }
    ],
    "name": "setAuthority",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "_keeper",
        "type": "address"
      },
      {
        "internalType": "bool",
        "name": "_auth",
        "type": "bool"
      }
    ],
    "name": "setKeeper",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
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
]"""


class TestContractSpec(TestCase):
    def test_abi(self) -> ContractSpec:
        contract = ContractSpec.from_json(
            ContractDefinition(
                "VolFeed",
                Address("0xf058Fe438AAF22617C30997579E89176e19635Dc")
            ),
            abi_json
        )
        # print(contract)
        return contract

    def test_contract(self) -> None:
        contract = self.test_abi()
        print(contract.generate_module_source())
