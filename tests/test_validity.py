import unittest

from hypothesis import given
from hypothesis.strategies import integers, decimals

from lsd import pounds_and_new_pence, pounds_shillings_and_pence


class TestSuccessfulConversion(unittest.TestCase):
    @given(
        l=integers(min_value=0),
        s=integers(min_value=0, max_value=19),
        d=decimals(min_value=0, max_value=11.99)
    )
    def test_convert_to_new_money(self, l, s, d):
        new_money = pounds_and_new_pence(l, s, d, rounding="nearest")
        self.assertIsNotNone(new_money)

    @given(
        p=decimals(min_value=0, allow_nan=False, allow_infinity=False)
    )
    def test_convert_to_old_money(self, p):
        old_money = pounds_shillings_and_pence(p, rounding="nearest")
        self.assertIsNotNone(old_money)
        self.assertEqual(len(old_money), 3)
