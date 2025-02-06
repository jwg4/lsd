## Converting to old money

```
>>> import lsd
>>> from decimal import Decimal
>>> lsd.pounds_shillings_and_pence(Decimal("1.49"), rounding="nearest", granularity="penny")
(1, 9, 10)
>>> lsd.pounds_shillings_and_pence(Decimal("1.49"), rounding="nearest")
(1, 9, 10)
>>> lsd.pounds_shillings_and_pence(Decimal("1.49"), rounding="fraction")
(1, 9, Decimal('9.60'))
>>> lsd.pounds_shillings_and_pence(Decimal("1.49"), rounding="strict")  # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
ConversionError: Using strict rounding, not an exact number of pennies.

>>> lsd.pounds_shillings_and_pence(Decimal("1.49"), rounding="nearest", granularity="hapenny")
(1, 9, 9.5)
>>> lsd.pounds_shillings_and_pence(Decimal("1.49"), rounding="nearest", granularity="farthing")
(1, 9, 9.5)

>>> lsd.pounds_shillings_and_pence(Decimal("1.49"), rounding="strict", granularity="hapenny")  # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
ConversionError: Using strict rounding, not an exact number of ha'pennies.
>>> lsd.pounds_shillings_and_pence(Decimal("1.49"), rounding="strict", granularity="farthing")  # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
ConversionError: Using strict rounding, not an exact number of farthings.

>>> lsd.pounds_shillings_and_pence(Decimal("0.0125"), rounding="strict", granularity="penny")
(0, 0, 3)
>>> lsd.pounds_shillings_and_pence(Decimal("0.05"), rounding="strict", granularity="penny")
(0, 1, 0)

>>> lsd.pounds_shillings_and_pence(Decimal("0.00625"), rounding="strict", granularity="penny")  # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
ConversionError: Using strict rounding, not an exact number of pennies.
>>> lsd.pounds_shillings_and_pence(Decimal("0.00625"), rounding="strict", granularity="hapenny")
(0, 0, 1.5)
>>> lsd.pounds_shillings_and_pence(Decimal("0.00625"), rounding="strict", granularity="farthing")
(0, 0, 1.5)

```

## Converting to new money

```
>>> import lsd
>>> lsd.pounds_and_new_pence(19, 19, 6)
Decimal('19.975')

>>> lsd.pounds_and_new_pence(19, 19, 6, rounding="nearest")
Decimal('19.975')
>>> lsd.pounds_and_new_pence(19, 19, 6, rounding="fraction")
Decimal('19.975')
>>> lsd.pounds_and_new_pence(19, 19, 6, rounding="strict")
Decimal('19.975')

```

The argument official, if set to True, will provide the rounding which was used officially when
the decimal switch took place. This meant rounding to even when the exact value was an odd number
of quarter pence. This only affects sums with either 3 or 9d, and means that the decimal conversions
of 3d and 9d sum to the decimal conversion of 1 shilling.

```
>>> lsd.pounds_and_new_pence(0, 0, 9, official=True)
Decimal('0.04')
>>> lsd.pounds_and_new_pence(0, 0, 3, official=True)
Decimal('0.01')

>>> lsd.pounds_and_new_pence(19, 19, 6, rounding="nearest", granularity="halfpenny")
Decimal('19.975')
>>> lsd.pounds_and_new_pence(19, 19, 6, rounding="nearest", granularity="penny")
Decimal('19.98')

>>> lsd.pounds_and_new_pence(19, 19, 6, rounding="strict", granularity="halfpenny")
Decimal('19.975')
>>> lsd.pounds_and_new_pence(19, 19, 6, rounding="strict", granularity="penny")  # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
ConversionError: Using strict rounding, not an exact number of new pence.

```

## Various completely wrong things
```
>>> lsd.pounds_shillings_and_pence(Decimal("0.00625"), rounding="strict", granularity="carrot")  # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
ArgumentError: Not a correct granularity specification: 'carrot'
>>> lsd.pounds_shillings_and_pence(Decimal("0.00625"), rounding="desiccant", granularity="farthing")  # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
ArgumentError: Not a correct rounding specification: 'desiccant'

>>> lsd.pounds_and_new_pence(19, 19, 6, rounding="strict", granularity="asdf")  # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
ArgumentError: Not a correct granularity specification: 'asdf'
>>> lsd.pounds_and_new_pence(19, 19, 6, rounding=4.4, granularity="penny")  # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
ArgumentError: Not a correct rounding specification: 4.4

```