
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

class optionHandler(BaseAbi):
    address: Address = Address("0x1F63F3B37f818f05ebefaCa11086e5250958e0D8")
    
    def authority(
        self,
    ) -> Address:
        return self._call(
            "authority"
        )
        
    def collateralAsset(
        self,
    ) -> Address:
        return self._call(
            "collateralAsset"
        )
        
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
        return self._call(
            "createOrder",
            _optionSeries=_optionSeries,
            _amount=_amount,
            _price=_price,
            _orderExpiry=_orderExpiry,
            _buyerAddress=_buyerAddress,
            _isBuyBack=_isBuyBack,
            _spotMovementRange=_spotMovementRange
        )
        
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
        return self._call(
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
        return self._call(
            "feePerContract"
        )
        
    def feeRecipient(
        self,
    ) -> Address:
        return self._call(
            "feeRecipient"
        )
        
    def liquidityPool(
        self,
    ) -> Address:
        return self._call(
            "liquidityPool"
        )
        
    def orderIdCounter(
        self,
    ) -> uint_e18:
        return self._call(
            "orderIdCounter"
        )
        
    def orderStores(
        self,
        x_0: uint_e18,
    ) -> tuple[Types_OptionSeries, uint_e18, uint_e18, uint_e18, Address, Address, uint128, uint128, bool]:
        return self._call(
            "orderStores",
            x_0=x_0
        )
        
    def protocol(
        self,
    ) -> Address:
        return self._call(
            "protocol"
        )
        
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
        return self._call(
            "strikeAsset"
        )
        
    def underlyingAsset(
        self,
    ) -> Address:
        return self._call(
            "underlyingAsset"
        )
    