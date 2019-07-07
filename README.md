# LSD - pounds, shillings and pence

[![PyPI](https://img.shields.io/pypi/v/lsd.svg)](https://pypi.python.org/pypi/lsd)
[![PyPI](https://img.shields.io/pypi/dm/lsd.svg)](https://pypi.python.org/pypi/lsd)
[![PyPI](https://img.shields.io/pypi/l/lsd.svg)](https://pypi.python.org/pypi/lsd)
[![Build Status](https://travis-ci.org/jwg4/lsd.svg?branch=master)](https://travis-ci.org/jwg4/lsd)

A library for converting between pre-decimal British currency and decimal ('new pence') currency.

## Usage
```
>>> import lsd
>>> from decimal import Decimal
>>> lsd.pounds_shillings_and_pence(Decimal("1.49"))
(1, 9, 10)
>>> lsd.pounds_and_new_pence(19, 19, 6)
Decimal('19.975')

```

For more usage examples, see the file examples.md

Calculations use the built-in Decimal class for amounts of pounds in new money. Calculation is thus dependent on the constraints of the Decimal class. This does not do arbitrary-precision arithmetic. Thus there are some numbers which are too big to be converted. You can alter these limits by setting the Decimal context in your own code.
See [[https://docs.python.org/2/library/decimal.html#context-objects]] or [[https://docs.python.org/3.7/library/decimal.html#context-objects]].

## Thanks
There are only six tests for this project. That's thanks to the awesome hypothesis project which generates test cases for unit tests. It's really powerful for checking edge cases. See [[https://github.com/HypothesisWorks/hypothesis]]