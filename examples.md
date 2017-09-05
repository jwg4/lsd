>>> import lsd
>>> from decimal import Decimal
>>> lsd.pounds_shillings_and_pence(Decimal("1.49"), rounding="nearest", granularity="penny")
(1, 9, 10)