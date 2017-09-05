from decimal import Decimal


def pounds_and_new_pence(l, s, d):
    l = Decimal(l)
    s = Decimal(s)
    d = Decimal(d)
    return l + s / 20 + d / 240


def pounds_shillings_and_pence(x, rounding="nearest", granularity="penny"):
    l = int(x)
    x = x - l
    s = int(x * 20)
    x = x * 20 - s
    if rounding == "nearest":
        d = int(round(x * 12))
    elif rounding == "fraction":
        d = x * 12
    elif rounding == "strict":
        raise Exception("Using strict rounding, not an exact number of pennies.")
    else:
        raise Exception("Not a correct rounding specification: %s." % rounding)
    return (l, s, d)
