from chain.config import Config
from chain.api.dhv import DhvChainReader
def test_config() -> Config:
    # TODO: remove! Should not have keys in code!
    return Config("hnzD3zyO8Ix97Akj37umR7ZdtaSW2xuC", "ARBITRUM_GOERLI")

if __name__ == "__main__":
    dhv = DhvChainReader.from_config(
        test_config())