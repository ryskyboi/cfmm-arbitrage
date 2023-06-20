
from chain.types import *
from chain.abi.types import *
from chain.abi.codegen import BaseAbi
from dataclasses import dataclass


        
@dataclass
class Types_OptionSeries:
    expiration: uint64
    strike: uint128
    isPut: bool
    underlying: Address
    strikeAsset: Address
    collateral: Address

    @classmethod
    def from_tuple(cls: type[Self], args: tuple) -> Self:
        return cls(
            uint64.from_tuple(args[0]),
            uint128.from_tuple(args[1]),
            bool(args[2]),
            Address.from_tuple(args[3]),
            Address.from_tuple(args[4]),
            Address.from_tuple(args[5]),
        )



class optionHandler(BaseAbi):
    address: Address = Address("0x1F63F3B37f818f05ebefaCa11086e5250958e0D8")
    
    def authority(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "authority"
        )
        return Address.from_tuple(my_var_0)
        
    def collateralAsset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "collateralAsset"
        )
        return Address.from_tuple(my_var_0)
        
    def createOrder(
        self,
        _optionSeries: Types_OptionSeries,
        _amount: uint_e18,
        _price: uint_e18,
        _orderExpiry: uint_e18,
        _buyerAddress: Address,
        _isBuyBack: bool,
        _spotMovementRange: list[uint_e18],
    ) -> uint_e18:
        my_var_0 = self._call(
            "createOrder",
            _optionSeries=_optionSeries,
            _amount=_amount,
            _price=_price,
            _orderExpiry=_orderExpiry,
            _buyerAddress=_buyerAddress,
            _isBuyBack=_isBuyBack,
            _spotMovementRange=_spotMovementRange
        )
        return uint_e18.from_tuple(my_var_0)
        
    def createStrangle(
        self,
        _optionSeriesCall: Types_OptionSeries,
        _optionSeriesPut: Types_OptionSeries,
        _amountCall: uint_e18,
        _amountPut: uint_e18,
        _priceCall: uint_e18,
        _pricePut: uint_e18,
        _orderExpiry: uint_e18,
        _buyerAddress: Address,
        _callSpotMovementRange: list[uint_e18],
        _putSpotMovementRange: list[uint_e18],
    ) -> tuple[uint_e18, uint_e18]:
        my_var_0, my_var_1 = self._call(
            "createStrangle",
            _optionSeriesCall=_optionSeriesCall,
            _optionSeriesPut=_optionSeriesPut,
            _amountCall=_amountCall,
            _amountPut=_amountPut,
            _priceCall=_priceCall,
            _pricePut=_pricePut,
            _orderExpiry=_orderExpiry,
            _buyerAddress=_buyerAddress,
            _callSpotMovementRange=_callSpotMovementRange,
            _putSpotMovementRange=_putSpotMovementRange
        )
        return uint_e18.from_tuple(my_var_0), uint_e18.from_tuple(my_var_1)
        
    def executeBuyBackOrder(
        self,
        _orderId: uint_e18,
    ) -> None:
        self._call(
            "executeBuyBackOrder",
            _orderId=_orderId
        )
        
    def executeOrder(
        self,
        _orderId: uint_e18,
    ) -> None:
        self._call(
            "executeOrder",
            _orderId=_orderId
        )
        
    def executeStrangle(
        self,
        _orderId1: uint_e18,
        _orderId2: uint_e18,
    ) -> None:
        self._call(
            "executeStrangle",
            _orderId1=_orderId1,
            _orderId2=_orderId2
        )
        
    def feePerContract(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "feePerContract"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def feeRecipient(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "feeRecipient"
        )
        return Address.from_tuple(my_var_0)
        
    def liquidityPool(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "liquidityPool"
        )
        return Address.from_tuple(my_var_0)
        
    def orderIdCounter(
        self,
    ) -> uint_e18:
        my_var_0 = self._call(
            "orderIdCounter"
        )
        return uint_e18.from_tuple(my_var_0)
        
    def orderStores(
        self,
        x_0: uint_e18,
    ) -> tuple[Types_OptionSeries, uint_e18, uint_e18, uint_e18, Address, Address, uint128, uint128, bool]:
        my_var_0, my_var_1, my_var_2, my_var_3, my_var_4, my_var_5, my_var_6, my_var_7, my_var_8 = self._call(
            "orderStores",
            x_0=x_0
        )
        return Types_OptionSeries.from_tuple(my_var_0), uint_e18.from_tuple(my_var_1), uint_e18.from_tuple(my_var_2), uint_e18.from_tuple(my_var_3), Address.from_tuple(my_var_4), Address.from_tuple(my_var_5), uint128.from_tuple(my_var_6), uint128.from_tuple(my_var_7), bool(my_var_8)
        
    def protocol(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "protocol"
        )
        return Address.from_tuple(my_var_0)
        
    def setAuthority(
        self,
        _newAuthority: Address,
    ) -> None:
        self._call(
            "setAuthority",
            _newAuthority=_newAuthority
        )
        
    def setFeePerContract(
        self,
        _feePerContract: uint_e18,
    ) -> None:
        self._call(
            "setFeePerContract",
            _feePerContract=_feePerContract
        )
        
    def setFeeRecipient(
        self,
        _feeRecipient: Address,
    ) -> None:
        self._call(
            "setFeeRecipient",
            _feeRecipient=_feeRecipient
        )
        
    def strikeAsset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "strikeAsset"
        )
        return Address.from_tuple(my_var_0)
        
    def underlyingAsset(
        self,
    ) -> Address:
        my_var_0 = self._call(
            "underlyingAsset"
        )
        return Address.from_tuple(my_var_0)
    