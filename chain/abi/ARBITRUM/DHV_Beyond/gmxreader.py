
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
class gmxreader(BaseAbi):
    address: Address = Address("0x22199a49a999c351ef7927602cfb187ec3cae489")
    
    def BASIS_POINTS_DIVISOR(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "BASIS_POINTS_DIVISOR"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def POSITION_PROPS_LENGTH(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "POSITION_PROPS_LENGTH"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def PRICE_PRECISION(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "PRICE_PRECISION"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def USDG_DECIMALS(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "USDG_DECIMALS"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getAmountOut(
        self,
        _vault: Address,
        _tokenIn: Address,
        _tokenOut: Address,
        _amountIn: uint_e18,
    ) -> tuple[uint_e18, uint_e18]:
        my_var_0, my_var_1 = self._call(
            "getAmountOut",
            _vault=_vault,
            _tokenIn=_tokenIn,
            _tokenOut=_tokenOut,
            _amountIn=_amountIn
        )
        return uint_e18.from_tuple(my_var_0), uint_e18.from_tuple(my_var_1)
        
    def getFeeBasisPoints(
        self,
        _vault: Address,
        _tokenIn: Address,
        _tokenOut: Address,
        _amountIn: uint_e18,
    ) -> tuple[uint_e18, uint_e18, uint_e18]:
        my_var_0, my_var_1, my_var_2 = self._call(
            "getFeeBasisPoints",
            _vault=_vault,
            _tokenIn=_tokenIn,
            _tokenOut=_tokenOut,
            _amountIn=_amountIn
        )
        return uint_e18.from_tuple(my_var_0), uint_e18.from_tuple(my_var_1), uint_e18.from_tuple(my_var_2)
        
    def getFees(
        self,
        _vault: Address,
        _tokens: list[Address],
    ) -> list[uint_e18]:
        my_var_0 = self._call(
            "getFees",
            _vault=_vault,
            _tokens=_tokens
        )
        return [uint_e18.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getFullVaultTokenInfo(
        self,
        _vault: Address,
        _weth: Address,
        _usdgAmount: uint_e18,
        _tokens: list[Address],
    ) -> list[uint_e18]:
        my_var_0 = self._call(
            "getFullVaultTokenInfo",
            _vault=_vault,
            _weth=_weth,
            _usdgAmount=_usdgAmount,
            _tokens=_tokens
        )
        return [uint_e18.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getFundingRates(
        self,
        _vault: Address,
        _weth: Address,
        _tokens: list[Address],
    ) -> list[uint_e18]:
        my_var_0 = self._call(
            "getFundingRates",
            _vault=_vault,
            _weth=_weth,
            _tokens=_tokens
        )
        return [uint_e18.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getMaxAmountIn(
        self,
        _vault: Address,
        _tokenIn: Address,
        _tokenOut: Address,
    ) -> uint_e18:
        my_var_0 = self._call(
            "getMaxAmountIn",
            _vault=_vault,
            _tokenIn=_tokenIn,
            _tokenOut=_tokenOut
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getPairInfo(
        self,
        _factory: Address,
        _tokens: list[Address],
    ) -> list[uint_e18]:
        my_var_0 = self._call(
            "getPairInfo",
            _factory=_factory,
            _tokens=_tokens
        )
        return [uint_e18.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getPositions(
        self,
        _vault: Address,
        _account: Address,
        _collateralTokens: list[Address],
        _indexTokens: list[Address],
        _isLong: list[bool],
    ) -> list[uint_e18]:
        my_var_0 = self._call(
            "getPositions",
            _vault=_vault,
            _account=_account,
            _collateralTokens=_collateralTokens,
            _indexTokens=_indexTokens,
            _isLong=_isLong
        )
        return [uint_e18.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getPrices(
        self,
        _priceFeed: Address,
        _tokens: list[Address],
    ) -> list[uint_e18]:
        my_var_0 = self._call(
            "getPrices",
            _priceFeed=_priceFeed,
            _tokens=_tokens
        )
        return [uint_e18.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getStakingInfo(
        self,
        _account: Address,
        _yieldTrackers: list[Address],
    ) -> list[uint_e18]:
        my_var_0 = self._call(
            "getStakingInfo",
            _account=_account,
            _yieldTrackers=_yieldTrackers
        )
        return [uint_e18.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getTokenBalances(
        self,
        _account: Address,
        _tokens: list[Address],
    ) -> list[uint_e18]:
        my_var_0 = self._call(
            "getTokenBalances",
            _account=_account,
            _tokens=_tokens
        )
        return [uint_e18.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getTokenBalancesWithSupplies(
        self,
        _account: Address,
        _tokens: list[Address],
    ) -> list[uint_e18]:
        my_var_0 = self._call(
            "getTokenBalancesWithSupplies",
            _account=_account,
            _tokens=_tokens
        )
        return [uint_e18.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getTokenSupply(
        self,
        _token: Address,
        _excludedAccounts: list[Address],
    ) -> uint_e18:
        my_var_0 = self._call(
            "getTokenSupply",
            _token=_token,
            _excludedAccounts=_excludedAccounts
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getTotalBalance(
        self,
        _token: Address,
        _accounts: list[Address],
    ) -> uint_e18:
        my_var_0 = self._call(
            "getTotalBalance",
            _token=_token,
            _accounts=_accounts
        )
        return uint_e18.from_tuple(my_var_0)
        
    def getTotalStaked(
        self,
        _yieldTokens: list[Address],
    ) -> list[uint_e18]:
        my_var_0 = self._call(
            "getTotalStaked",
            _yieldTokens=_yieldTokens
        )
        return [uint_e18.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getVaultTokenInfo(
        self,
        _vault: Address,
        _weth: Address,
        _usdgAmount: uint_e18,
        _tokens: list[Address],
    ) -> list[uint_e18]:
        my_var_0 = self._call(
            "getVaultTokenInfo",
            _vault=_vault,
            _weth=_weth,
            _usdgAmount=_usdgAmount,
            _tokens=_tokens
        )
        return [uint_e18.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getVaultTokenInfoV2(
        self,
        _vault: Address,
        _weth: Address,
        _usdgAmount: uint_e18,
        _tokens: list[Address],
    ) -> list[uint_e18]:
        my_var_0 = self._call(
            "getVaultTokenInfoV2",
            _vault=_vault,
            _weth=_weth,
            _usdgAmount=_usdgAmount,
            _tokens=_tokens
        )
        return [uint_e18.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def getVestingInfo(
        self,
        _account: Address,
        _vesters: list[Address],
    ) -> list[uint_e18]:
        my_var_0 = self._call(
            "getVestingInfo",
            _account=_account,
            _vesters=_vesters
        )
        return [uint_e18.from_tuple(arg_0) for arg_0 in my_var_0]
        
    def gov(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "gov"
        )
        return Address.from_tuple(my_var_0)
        
    def hasMaxGlobalShortSizes(
        self,
    ) -> bool:
        my_var_0 = self._call(
            "hasMaxGlobalShortSizes"
        )
        return bool(my_var_0)
        
    def setConfig(
        self,
        _hasMaxGlobalShortSizes: bool,
    ) -> None:
        self._call(
            "setConfig",
            _hasMaxGlobalShortSizes=_hasMaxGlobalShortSizes
        )
        
    def setGov(
        self,
        _gov: Address,
    ) -> None:
        self._call(
            "setGov",
            _gov=_gov
        )
    