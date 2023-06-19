from chain.api.dhv import DhvChainReader
from chain.config import Config

def test_config() -> Config:
    # TODO: remove! Should not have keys in code!
    return Config("hnzD3zyO8Ix97Akj37umR7ZdtaSW2xuC", "ARBITRUM_GOERLI")

def get_spread():
    dhv = DhvChainReader.from_config(test_config())
    return dhv.position_data()


if __name__ == "__main__":
    print(get_spread())