from __future__ import division
from decimal import Decimal

from .constants import PENCE
from .error import ConversionError, ArgumentError
from .helpers import _get_granularity_multiplier, _strict_rounding


def pounds_and_new_pence(l, s, d, rounding="nearest", granularity="halfpenny"):
    l = Decimal(l)
    s = Decimal(s)
    d = Decimal(d)
    exact = l + s / 20 + d / 240
    multiplier = Decimal(_get_granularity_multiplier(granularity))
    if rounding == "nearest":
        return (exact * multiplier).quantize(PENCE) / multiplier
    if rounding == "strict":
        pence = exact * multiplier * 100
        if pence != int(pence):
            raise ConversionError(granularity, decimal=True)
        return pence / (100 * multiplier)
    elif rounding == "fraction":
        return exact
    else:
        raise ArgumentError("rounding", rounding)


def pounds_shillings_and_pence(x, rounding="nearest", granularity="penny"):
    l = int(x)
    x = x - l
    s = int(x * 20)
    x = x * 20 - s

    k = _get_granularity_multiplier(granularity)

    if rounding == "nearest":
        d = round(x * 12 * k) / k
        if k == 1:
            d = int(d)
    elif rounding == "fraction":
        d = x * 12
    elif rounding == "strict":
        d = _strict_rounding(x, k, granularity)
    else:
        raise ArgumentError("rounding", rounding)
    return (l, s, d)
