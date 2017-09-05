# LSD - pounds, shillings and pence

A library for converting between pre-decimal British currency and decimal ('new pence') currency.

## Usage
>>> import lsd
>>> from decimal import Decimal
>>> lsd.pounds_shillings_and_pence(Decimal("1.49"))
(1, 9, 10)
>>> lsd.pounds_and_pence(19, 19, 6)
Decimal("19.975")
