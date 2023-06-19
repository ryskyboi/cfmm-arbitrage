from unittest import TestCase
from chain.config import Config
from chain.api.dhv import DhvChainReader
from chain.api.dhv.spreadparams import FeeIvSpreadParams, CollateralSpreadParams,\
    DeltaSpreadParams
from chain.api.dhv.collatparams import CollateralParams
from chain.api.dhv.slippageparams import SlippageParams

#slippage
putSlippageGradinetMultipliers=  [ 32.062695776005754, 31.993108078547117, 31.810983791965135, 31.43481548633707, 30.974590543073322, 30.668836938634346, 30.604289472424558, 30.37288983067886, 30.030481446713097, 29.992446607725974, 29.813904329921087, 29.50780508052873, 29.31535898140196, 29.626966203258913, 30.089132194169007, 29.09819765692076, 29.41624225234537, 29.3254848787627, 29.080503786931374, 28.890374184496547]
callSlippageGradinetMultipliers = [ 32.03079203078064, 31.878274585633, 31.586021183324043, 31.154469238517148, 30.61983012863621, 30.02751862352724, 29.767935988773843, 29.519651037986595, 29.275896521840654, 29.158132246914192, 28.899189048089795, 28.79395354628805, 28.59621097502779, 28.531936098531766, 28.496474210701045, 28.672129637088712, 28.553187694507074, 28.461496570374543, 28.409699162604046, 28.357901754833552]
slippageGradient =  0.0001

slippage_params = SlippageParams(putSlippageGradinetMultipliers,
                                 callSlippageGradinetMultipliers,
                                 slippageGradient)
##collat
callSpotShock =  1.0
callPremiumCurve = {
    7.0: 0.137310398921181,
    14.0: 0.21532271007278916,
    28.0: 0.28537036027751395,
    42.0: 0.3483113205978359,
    56.0: 0.42147556914068085,
    70.0: 0.4905540584029809,
    84.0: 0.5301302667777277
}
putSpotShock = 1.0
putPremiumCurve = {
    7.0: 0.16097528948543374,
    14.0: 0.23027824327552782,
    28.0: 0.3056523951032439,
    42.0: 0.3808216700904456,
    56.0: 0.4539548883445394,
    70.0: 0.5238145515841939,
    84.0: 0.5678502236865992
}

collat_params = CollateralParams(callSpotShock,
                                 callPremiumCurve,
                                 putSpotShock,
                                 putPremiumCurve)
#spread
fee_dollar = 0.5
iv_relative_spread = 0.0
collateral_rate = 0.04
dhv_buy_call_rate = 0.0195
dhv_buy_put_rate = 0.015
dhv_sell_call_rate = 0.015
dhv_sell_put_rate = 0.0195
dhv_borrow_rates = [dhv_buy_call_rate, dhv_buy_put_rate, dhv_sell_call_rate, dhv_sell_put_rate]

collat_spread_params = CollateralSpreadParams(collateral_rate)
fee_iv_spread_params = FeeIvSpreadParams(fee_dollar, iv_relative_spread)
delta_spread_params = DeltaSpreadParams(dhv_borrow_rates[1], dhv_borrow_rates[0], dhv_borrow_rates[2], dhv_borrow_rates[3])


def test_config() -> Config:
    # TODO: remove! Should not have keys in code!
    return Config("hnzD3zyO8Ix97Akj37umR7ZdtaSW2xuC", "ARBITRUM_GOERLI")

class TestDhvChainReader(TestCase):
    def test_data(self):
        dhv = DhvChainReader.from_config(
            test_config()
        )
        self.assertTrue( slippage_params == dhv.slippage_param_data(),
                        "... slippage fail")

        self.assertTrue( collat_params == dhv.collat_param_data(),
                        "... collat fail")

        self.assertTrue( collat_spread_params == dhv.delta_spread_param_data(),
                        "... delta spread fail")

        self.assertTrue( fee_iv_spread_params == dhv.fee_iv_spread_param_data(),
                        "... fee iv spread fail")

        self.assertTrue( delta_spread_params == dhv.delta_spread_param_data(),
                        "... delta spread fail")
