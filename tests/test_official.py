import unittest

from decimal import Decimal

from lsd import pounds_and_new_pence


class TestOfficialToDecimal(unittest.TestCase):
    """
        These are official examples given by leaflets at the time of
        Decimal Day in 1971. By default, we should convert these amounts
        correctly.
    """
    def test_official_shillings(self):
        self.assertEqual(Decimal('0.05'), pounds_and_new_pence(0, 1, 0))
        self.assertEqual(Decimal('0.25'), pounds_and_new_pence(0, 5, 0))
        self.assertEqual(Decimal('0.50'), pounds_and_new_pence(0, 10, 0))
        self.assertEqual(Decimal('0.60'), pounds_and_new_pence(0, 12, 0))
        self.assertEqual(Decimal('0.95'), pounds_and_new_pence(0, 19, 0))

    def test_official_pence(self):
        self.assertEqual(Decimal('0.005'), pounds_and_new_pence(0, 0, 1))
        self.assertEqual(Decimal('0.01'), pounds_and_new_pence(0, 0, 2))
        self.assertEqual(Decimal('0.01'), pounds_and_new_pence(0, 0, 3))
        self.assertEqual(Decimal('0.015'), pounds_and_new_pence(0, 0, 4))
        self.assertEqual(Decimal('0.02'), pounds_and_new_pence(0, 0, 5))
        self.assertEqual(Decimal('0.025'), pounds_and_new_pence(0, 0, 6))
