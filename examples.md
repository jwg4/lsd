>>> import lsd
>>> from decimal import Decimal
>>> lsd.pounds_shillings_and_pence(Decimal("1.49"), rounding="nearest", granularity="penny")
(1, 9, 10)
>>> lsd.pounds_shillings_and_pence(Decimal("1.49"), rounding="nearest")
(1, 9, 10)
>>> lsd.pounds_shillings_and_pence(Decimal("1.49"), rounding="fraction")
(1, 9, Decimal('9.60'))
>>> lsd.pounds_shillings_and_pence(Decimal("1.49"), rounding="strict")
Traceback (most recent call last):
...
Exception: Using strict rounding, not an exact number of pennies.

>>> lsd.pounds_shillings_and_pence(Decimal("1.49"), rounding="nearest", granularity="hapenny")
(1, 9, 9.5)
>>> lsd.pounds_shillings_and_pence(Decimal("1.49"), rounding="nearest", granularity="farthing")
(1, 9, 9.5)

>>> lsd.pounds_shillings_and_pence(Decimal("1.49"), rounding="strict", granularity="hapenny")
Traceback (most recent call last):
...
Exception: Using strict rounding, not an exact number of pennies.
>>> lsd.pounds_shillings_and_pence(Decimal("1.49"), rounding="strict", granularity="farthing")
Traceback (most recent call last):
...
Exception: Using strict rounding, not an exact number of pennies.
