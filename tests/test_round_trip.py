import unittest

from hypothesis import given
from hypothesis.strategies import integers, decimals

from lsd import pounds_and_new_pence, pounds_shillings_and_pence


class TestRoundTrips(unittest.TestCase):
    @given(
        l=integers(min_value=0, max_value=100),
        s=integers(min_value=0, max_value=19),
        d=decimals(min_value=0, max_value=11.99)
    )
    def test_round_trip(self, l, s, d):
        new_money = pounds_and_new_pence(l, s, d)
        l_, s_, d_ = pounds_shillings_and_pence(new_money, rounding="fraction")
        self.assertEqual(l_, l)
        self.assertEqual(s_, s)
        self.assertAlmostEqual(d_, d)
