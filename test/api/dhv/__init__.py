from unittest import TestCase
from datetime import datetime as dt
from chain.api.dhv import DhvChainReader
from chain.api.reader import ChainReader
from chain.api.dhv.spreadparams import FeeIvSpreadParams, CollateralSpreadParams,\
    DeltaSpreadParams
from chain.api.dhv.positions import Positions, Position
from chain.api.dhv.collatparams import CollateralParams
from chain.api.dhv.slippageparams import SlippageParams
from chain.api.dhv import SabrExpiryParams, SabrModelParam
from chain.config import Config

def test_config() -> Config:
    # TODO: remove! Should not have keys in code!
    return Config("hnzD3zyO8Ix97Akj37umR7ZdtaSW2xuC", "ARBITRUM_GOERLI")

x = 1686323853.719705
r = .05
a = .25
b = .99
p = -.5
n = .35

##slippage
putSlippageGradinetMultipliers=  [ 32.062695776005754, 31.993108078547117, 31.810983791965135,
                                  31.43481548633707, 30.974590543073322, 30.668836938634346,
                                  30.604289472424558, 30.37288983067886, 30.030481446713097,
                                  29.992446607725974, 29.813904329921087, 29.50780508052873,
                                  29.31535898140196, 29.626966203258913, 30.089132194169007,
                                  29.09819765692076, 29.41624225234537, 29.3254848787627,
                                  29.080503786931374, 28.890374184496547]
callSlippageGradinetMultipliers = [ 32.03079203078064, 31.878274585633, 31.586021183324043,
                                   31.154469238517148, 30.61983012863621, 30.02751862352724,
                                   29.767935988773843, 29.519651037986595, 29.275896521840654,
                                   29.158132246914192, 28.899189048089795, 28.79395354628805,
                                   28.59621097502779, 28.531936098531766, 28.496474210701045,
                                   28.672129637088712, 28.553187694507074, 28.461496570374543,
                                   28.409699162604046, 28.357901754833552]
slippageGradient =  0.0001

##collat
callSpotShock =  1.0,
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
    7.0: 0.137310398921181,
    14.0: 0.21532271007278916,
    28.0: 0.28537036027751395,
    42.0: 0.3483113205978359,
    56.0: 0.42147556914068085,
    70.0: 0.4905540584029809,
    84.0: 0.5301302667777277
}
#spread
fee_dollar = 0.5
iv_relative_spread = 0
collateral_rate = 0.04
dhv_buy_call_rate = 0.015
dhv_buy_put_rate = 0.0195
dhv_sell_call_rate = 0.015
dhv_sell_put_rate = 0.0195
dhv_borrow_rates = [dhv_buy_call_rate, dhv_buy_put_rate, dhv_sell_call_rate, dhv_sell_put_rate]

#collat
callSpotShock = 1.0,
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
    7.0: 0.137310398921181,
    14.0: 0.21532271007278916,
    28.0: 0.28537036027751395,
    42.0: 0.3483113205978359,
    56.0: 0.42147556914068085,
    70.0: 0.4905540584029809,
    84.0: 0.5301302667777277
}
#Positions
positions = [Position(expiry_timestamp_s=1688112000, is_call=True, strike=1700.0, position=-144.3),
             Position(expiry_timestamp_s=1688112000, is_call=True, strike=1800.0, position=77.0),
             Position(expiry_timestamp_s=1688112000, is_call=True, strike=1900.0, position=-185.67),
             Position(expiry_timestamp_s=1688112000, is_call=True, strike=2000.0, position=-231.64),
             Position(expiry_timestamp_s=1688112000, is_call=True, strike=2100.0, position=-488.46),
             Position(expiry_timestamp_s=1688112000, is_call=True, strike=2200.0, position=-499.9),
             Position(expiry_timestamp_s=1688112000, is_call=True, strike=1600.0, position=0.0),
             Position(expiry_timestamp_s=1688112000, is_call=True, strike=1500.0, position=0.0),
             Position(expiry_timestamp_s=1688112000, is_call=False, strike=1700.0,
                      position=-195.75321988752353),
             Position(expiry_timestamp_s=1688112000, is_call=False, strike=1800.0, position=-159.0),
             Position(expiry_timestamp_s=1688112000, is_call=False, strike=1900.0, position=-28.09),
             Position(expiry_timestamp_s=1688112000, is_call=False, strike=2000.0, position=-6.54),
             Position(expiry_timestamp_s=1688112000, is_call=False, strike=2100.0, position=0.0),
             Position(expiry_timestamp_s=1688112000, is_call=False, strike=2200.0, position=0.0),
             Position(expiry_timestamp_s=1688112000, is_call=False, strike=1600.0,
                      position=-246.21470804373016),
             Position(expiry_timestamp_s=1688112000, is_call=False, strike=1500.0, position=-393.5),
             Position(expiry_timestamp_s=1687507200, is_call=True, strike=1700.0, position=0.0),
             Position(expiry_timestamp_s=1687507200, is_call=True, strike=1750.0, position=0.0),
             Position(expiry_timestamp_s=1687507200, is_call=True, strike=1800.0, position=-30.0),
             Position(expiry_timestamp_s=1687507200, is_call=True, strike=1850.0, position=-100.0),
             Position(expiry_timestamp_s=1687507200, is_call=True, strike=1900.0, position=-100.0),
             Position(expiry_timestamp_s=1687507200, is_call=True, strike=1950.0, position=-216.58),
             Position(expiry_timestamp_s=1687507200, is_call=True, strike=2000.0, position=-350.42),
             Position(expiry_timestamp_s=1687507200, is_call=True, strike=2050.0, position=0.0),
             Position(expiry_timestamp_s=1687507200, is_call=True, strike=2100.0, position=0.0),
             Position(expiry_timestamp_s=1687507200, is_call=False, strike=1700.0, position=-100.0),
             Position(expiry_timestamp_s=1687507200, is_call=False, strike=1750.0, position=-100.0),
             Position(expiry_timestamp_s=1687507200, is_call=False, strike=1800.0, position=-100.0),
             Position(expiry_timestamp_s=1687507200, is_call=False, strike=1850.0, position=-100.0),
             Position(expiry_timestamp_s=1687507200, is_call=False, strike=1900.0, position=-18.5),
             Position(expiry_timestamp_s=1687507200, is_call=False, strike=1950.0, position=0.0),
             Position(expiry_timestamp_s=1687507200, is_call=False, strike=2000.0, position=0.0),
             Position(expiry_timestamp_s=1687507200, is_call=False, strike=2050.0, position=0.0),
             Position(expiry_timestamp_s=1687507200, is_call=False, strike=2100.0, position=0.0)]

#This doesn't conform to PEP8 but trying to make it look reasonableis taking ages
positions_from_chain = ([1688112000, 1686902400, 1687507200], [(1688112000, [1700000000000000000000, 1800000000000000000000, 1900000000000000000000, 2000000000000000000000, 2100000000000000000000, 2200000000000000000000, 1600000000000000000000, 1500000000000000000000], [(1700000000000000000000, (388810010046517632, 40670661, 500000, False, False), (388810010046517632, 42197129, 500000, False, False), 329973294863885191, -144300000000000000000), (1800000000000000000000, (417629055969792378, 7279166, 500000, False, False), (417629055969792378, 7580616, 500000, False, False), 139765788487174936, 77000000000000000000), (1900000000000000000000, (467048001390661856, 7275625, 500000, True, False), (467048001390661856, 8172294, 500000, True, False), 62954772831228782, -185670000000000000000), (2000000000000000000000, (519818184635781905, 4293655, 500000, True, False), (519818184635781905, 5119049, 500000, True, False), 31918656491452468, -231640000000000000000), (2100000000000000000000, (571138377347954056, 5586300, 500000, True, False), (571138377347954056, 6387863, 500000, True, False), 17878834707336788, -488460000000000000000), (2200000000000000000000, (619821322335253972, 3586617, 500000, True, True), (619821322335253972, 4367703, 500000, True, False), 10816118468935972, -499900000000000000000), (1600000000000000000000, (413359620438031088, 73742185, 500000, False, False), (413359620438031088, 75985743, 500000, False, False), 624311372321320709, 0), (1500000000000000000000, (486726307611261874, 151770281, 500000, True, False), (486726307611261874, 154752880, 500000, True, False), 826141229581625121, 0)], [1700000000000000000000, 1800000000000000000000, 1900000000000000000000, 2000000000000000000000, 2100000000000000000000, 2200000000000000000000, 1600000000000000000000, 1500000000000000000000], [(1700000000000000000000, (388810010046517632, 158610980, 500000, False, False), (388810010046517632, 161716514, 500000, False, False), -670026705136114810, -195753219887523536000), (1800000000000000000000, (417629055969792378, 272718706, 500000, True, False), (417629055969792378, 276805844, 500000, True, False), -860234211512825064, -159000000000000000000), (1900000000000000000000, (467048001390661856, 287699566, 500000, True, False), (467048001390661856, 292182302, 500000, True, False), -937045227168771218, -28090000000000000000), (2000000000000000000000, (519818184635781905, 369734687, 500000, True, False), (519818184635781905, 374689382, 500000, True, False), -968081343508547532, -6540000000000000000), (2100000000000000000000, (571138377347954056, 461667109, 500000, True, False), (571138377347954056, 467083929, 500000, True, False), -982121165292663212, 0), (2200000000000000000000, (619821322335253972, 560981384, 500000, True, False), (619821322335253972, 566863626, 500000, True, False), -989183881531064029, 0), (1600000000000000000000, (413359620438031088, 78137031, 500000, False, False), (413359620438031088, 80128948, 500000, False, False), -375688627678679292, -246214708043730166000), (1500000000000000000000, (486726307611261874, 53821546, 500000, False, False), (486726307611261874, 55174770, 500000, False, False), -173858770418374879, -393500000000000000000)], 1635797030000000000000), (1686902400, [2050000000000000000000, 2000000000000000000000, 1950000000000000000000, 1900000000000000000000, 1850000000000000000000, 1800000000000000000000, 1750000000000000000000], [(2050000000000000000000, (889716519213484138, 10, 500000, True, True), (889716519213484138, 21993, 500000, True, True), 220853036916, -401000000000000000000), (2000000000000000000000, (830657570271372805, 47, 500000, True, True), (830657570271372805, 22030, 500000, True, True), 728179140740, -510000000000000000000), (1950000000000000000000, (768944957030861138, 98, 500000, True, True), (768944957030861138, 22081, 500000, True, True), 2709353439313, -332580000000000000000), (1900000000000000000000, (704442597421111086, 346, 500000, True, True), (704442597421111086, 22331, 500000, True, True), 11706192154672, -276560000000000000000), (1850000000000000000000, (637185231964021683, 762, 500000, True, True), (637185231964021683, 22755, 500000, True, True), 61072136709455, -13750000000000000000), (1800000000000000000000, (567776048111252247, 5663, 500000, True, True), (567776048111252247, 27713, 500000, True, True), 405344370262044, -50060000000000000000), (1750000000000000000000, (498821239543237299, 44717, 500000, True, True), (498821239543237299, 67285, 500000, True, True), 3623947409968900, 0)], [2050000000000000000000, 2000000000000000000000, 1950000000000000000000, 1900000000000000000000, 1850000000000000000000, 1800000000000000000000, 1750000000000000000000], [(2050000000000000000000, (889716519213484138, 412982455, 500000, True, False), (889716519213484138, 414399773, 500000, True, False), -999999779146963084, 0), (2000000000000000000000, (830657570271372805, 363067802, 500000, True, False), (830657570271372805, 364336021, 500000, True, False), -999999271820859260, 0), (1950000000000000000000, (768944957030861138, 407187559, 500000, True, False), (768944957030861138, 408578347, 500000, True, False), -999997290646560688, -91000000000000000000), (1900000000000000000000, (704442597421111086, 263238618, 500000, True, False), (704442597421111086, 264208637, 500000, True, False), -999988293807845328, 0), (1850000000000000000000, (637185231964021683, 375578292, 500000, True, False), (637185231964021683, 376867964, 500000, True, False), -999938927863290545, -196020000000000000000), (1800000000000000000000, (567776048111252247, 168199285, 500000, True, False), (567776048111252247, 168884883, 500000, True, False), -999594655629737957, -10000000000000000000), (1750000000000000000000, (498821239543237299, 203993556, 500000, True, False), (498821239543237299, 204777164, 500000, True, False), -996376052590031100, -203000000000000000000)], 1635797030000000000000), (1687507200, [1700000000000000000000, 1750000000000000000000, 1800000000000000000000, 1850000000000000000000, 1900000000000000000000, 1950000000000000000000, 2000000000000000000000, 2050000000000000000000, 2100000000000000000000], [(1700000000000000000000, (398743377170208884, 15197775, 500000, False, False), (398743377170208884, 15827667, 500000, False, False), 269589224375318926, 0), (1750000000000000000000, (419083627572790013, 7323097, 500000, False, False), (419083627572790013, 7800475, 500000, False, False), 146557803251237884, 0), (1800000000000000000000, (450101472822761301, 4211284, 500000, True, False), (450101472822761301, 4609457, 500000, True, False), 80798826786577757, -30000000000000000000), (1850000000000000000000, (485185618355956879, 2998515, 500000, True, True), (485185618355956879, 3356880, 500000, True, True), 46748714409792325, -100000000000000000000), (1900000000000000000000, (521311261968496605, 1825746, 500000, True, True), (521311261968496605, 2161058, 500000, True, True), 28490297527880314, -100000000000000000000), (1950000000000000000000, (557181306935093274, 1710992, 500000, True, True), (557181306935093274, 2035053, 500000, True, True), 18193572029888635, -216580000000000000000), (2000000000000000000000, (592243783419753621, 1770860, 500000, True, True), (592243783419753621, 2088666, 500000, True, True), 12093489622593515, -350420000000000000000), (2050000000000000000000, (626274127422443931, 400221, 500000, True, True), (626274127422443931, 709646, 500000, True, True), 8317283119120232, 0), (2100000000000000000000, (659197504581035125, 288003, 500000, True, True), (659197504581035125, 594501, 500000, True, True), 5888702556444682, 0)], [1700000000000000000000, 1750000000000000000000, 1800000000000000000000, 1850000000000000000000, 1900000000000000000000, 1950000000000000000000, 2000000000000000000000, 2050000000000000000000, 2100000000000000000000], [(1700000000000000000000, (398743377170208884, 105092131, 500000, True, False), (398743377170208884, 106784360, 500000, True, False), -730410775624681074, -100000000000000000000), (1750000000000000000000, (419083627572790013, 160433603, 500000, True, False), (419083627572790013, 162491209, 500000, True, False), -853442196748762116, -100000000000000000000), (1800000000000000000000, (450101472822761301, 221973207, 500000, True, False), (450101472822761301, 224338466, 500000, True, False), -919201173213422243, -100000000000000000000), (1850000000000000000000, (485185618355956879, 285875461, 500000, True, False), (485185618355956879, 288510274, 500000, True, False), -953251285590207675, -100000000000000000000), (1900000000000000000000, (521311261968496605, 277549174, 500000, True, False), (521311261968496605, 280227456, 500000, True, False), -971509702472119687, -18500000000000000000), (1950000000000000000000, (557181306935093274, 312497794, 500000, True, False), (557181306935093274, 315333653, 500000, True, False), -981806427970111365, 0), (2000000000000000000000, (592243783419753621, 362103325, 500000, True, False), (592243783419753621, 365133352, 500000, True, False), -987906510377406486, 0), (2050000000000000000000, (626274127422443931, 411816801, 500000, True, False), (626274127422443931, 415038123, 500000, True, False), -991682716880879768, 0), (2100000000000000000000, (659197504581035125, 461592611, 500000, True, False), (659197504581035125, 465003561, 500000, True, False), -994111297443555318, 0)], 1635797030000000000000)])


class MockDhvChainReader(DhvChainReader):
    def __init__(self):
        pass

    def expiry_timestamps_s(self, is_include_expired=False) -> list[int]:
        return [0]

    def sabr_param_data(self, is_include_expired=False) -> list[SabrExpiryParams]:
        sabrs: list[SabrExpiryParams] = []
        for t in self.expiry_timestamps_s(is_include_expired):
            sabrs.append(
                SabrExpiryParams(
                    t,
                    SabrModelParam(
                        a,
                        b,
                        p,
                        n,
                    ),
                    SabrModelParam(
                        a,
                        b,
                        p,
                        n,
                    ),
                    float(r)
                )
            )
        return sabrs

    def fee_iv_spread_param_data(self) -> FeeIvSpreadParams:
        """returns: feeivspreadparsms contains a fee per contract a relative myltiplier
        that allows us to pay less in IV than we buy it for
        """
        fee_per_contract = fee_dollar
        return FeeIvSpreadParams(fee_per_contract,
                                 iv_relative_spread)

    def delta_spread_param_data(self) -> DeltaSpreadParams:
        """returns: delta_spread_params contains 4 rates charged when buying/sellig
        calls and puts and their related hedging activities"""
        delta_borrow_rates = dhv_borrow_rates
        return DeltaSpreadParams(delta_borrow_rates[1],
                                  delta_borrow_rates[0],
                                  delta_borrow_rates[2],
                                  delta_borrow_rates[3])

    def collat_spread_param_data(self) -> CollateralSpreadParams:
        """returns: collat_spread_params contains the rate paid on collat that the
        DHV has to lock up"""
        collat_lending_rate = collateral_rate
        return CollateralSpreadParams(collat_lending_rate)


    def position_data(self) -> Positions:
        from chain.abi.types import cast_e18_to_float
        _position_data : Positions = []
        option_chain = positions_from_chain
        data = option_chain[1]
        for _by_expiration in data:
            expiry = _by_expiration[0]
            for _by_strike_calls in _by_expiration[2]:
                strike = cast_e18_to_float(_by_strike_calls[0])
                _position_data.append(Position(expiry, True, strike,
                                               cast_e18_to_float(_by_strike_calls[4])))
            for _by_strike_puts in _by_expiration[4]:
                strike = cast_e18_to_float(_by_strike_puts[0])
                _position_data.append(Position(expiry, False, strike,
                                               cast_e18_to_float(_by_strike_puts[4])))
        return _position_data

    def collat_param_data(self, is_usd_collateral: bool = False) -> CollateralParams:
        call_spot_shock = callSpotShock
        put_spot_shock = putSpotShock
        times_to_exp_calls = [x*(60**2)*24 for x in callPremiumCurve]
        times_to_exp_puts = [x*(60**2)*24 for x in putPremiumCurve]
        max_prices_calls = [callPremiumCurve[t/(60*60*24)] for t in times_to_exp_calls]
        max_prices_puts = [putPremiumCurve[t/(60*60*24)] for t in times_to_exp_puts]
        return CollateralParams(call_spot_shock,
                                dict(zip([t/(60*60*24) for t in times_to_exp_calls], max_prices_calls)),
                                put_spot_shock,
                                dict(zip([t/(60*60*24) for t in times_to_exp_puts], max_prices_puts)))

    def slippage_param_data(self) -> SlippageParams:
        call_slippage_gradient_multipliers = callSlippageGradinetMultipliers
        put_slippage_gradient_multipliers = putSlippageGradinetMultipliers
        slippage_gradient = slippageGradient
        return SlippageParams([multiplier for multiplier in put_slippage_gradient_multipliers],
                              [multiplier for multiplier in call_slippage_gradient_multipliers],
                              slippage_gradient)


class TestDhvChainReader(TestCase):
    def test_data(self):
        chain_reader = MockDhvChainReader()

        #spread
        collat_spread_params = CollateralSpreadParams(collateral_rate)
        fee_iv_spread_params = FeeIvSpreadParams(fee_dollar,
                                                 iv_relative_spread)
        delta_spread_params = DeltaSpreadParams(dhv_borrow_rates[1],
                                                dhv_borrow_rates[0],
                                                dhv_borrow_rates[2],
                                                dhv_borrow_rates[3])


        self.assertTrue( collat_spread_params == chain_reader.collat_spread_param_data(),
                        "... spread fail")

        self.assertTrue( fee_iv_spread_params == chain_reader.fee_iv_spread_param_data(),
                        "... spread fail")

        self.assertTrue( delta_spread_params == chain_reader.delta_spread_param_data(),
                        "... spread fail")

        #collat
        collat_params = CollateralParams(callSpotShock,
                                         callPremiumCurve,
                                         putSpotShock,
                                         putPremiumCurve)
        self.assertTrue( collat_params == chain_reader.collat_param_data(),
                        "... collat fail")

        #slippage
        slippage_params = SlippageParams(putSlippageGradinetMultipliers,
                                         callSlippageGradinetMultipliers,
                                         slippageGradient)

        self.assertTrue( slippage_params == chain_reader.slippage_param_data(),
                        "... slippage fail")

        #position
        def find_same_pos(position):
            if len([x for x in chain_reader.position_data() if
             (x.is_call == position.is_call and
              x.expiry_timestamp_s == position.expiry_timestamp_s and
              x.strike == position.strike and
              x.position == position.position)]) > 0:
                return True
            else:
                return position

        self.assertTrue([find_same_pos(pos) for pos in positions],
                        "... position fail")


        #sabr
        sab = [SabrExpiryParams(0,SabrModelParam( a, b, p, n),SabrModelParam( a, b, p, n),float(r))]

        self.assertTrue(sab == chain_reader.sabr_param_data(),
                        "... sabr fail")




if __name__ == "__main__":
    test= TestDhvChainReader()
    test.test_data()