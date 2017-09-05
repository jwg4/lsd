# LSD - pounds, shillings and pence

[![PyPI](https://img.shields.io/pypi/v/lsd.svg)](https://pypi.python.org/pypi/lsd)
[![PyPI](https://img.shields.io/pypi/dm/lsd.svg)](https://pypi.python.org/pypi/lsd)
[![PyPI](https://img.shields.io/pypi/l/lsd.svg)](https://pypi.python.org/pypi/lsd)
[![Build Status](https://travis-ci.org/jwg4/lsd.svg?branch=master)](https://travis-ci.org/jwg4/lsd)

A library for converting between pre-decimal British currency and decimal ('new pence') currency.

## Usage
>>> import lsd
>>> from decimal import Decimal
>>> lsd.pounds_shillings_and_pence(Decimal("1.49"))
(1, 9, 10)
>>> lsd.pounds_and_new_pence(19, 19, 6)
Decimal('19.975')

For more usage examples, see the file examples.md
