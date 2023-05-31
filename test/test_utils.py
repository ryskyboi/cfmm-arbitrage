from chain.api.dhv import DhvChainReader
from test import test_config

dhv = DhvChainReader.from_config(test_config())
abi = dhv.vol_feed.abi_json
print(dhv.vol_feed._w3_contract.address)
for a in abi:
    if a['type'] == "function":
        print(a['name'])

