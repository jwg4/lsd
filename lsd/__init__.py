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

    if granularity == "penny":
        k = 1
    elif granularity == "hapenny":
        k = 2
    elif granularity == "farthing":
        k = 4
    else:
        raise Exception("Not a correct granularity specification: %s." % granularity)

    if rounding == "nearest":
        d = round(x * 12 * k) / k
        if k == 1:
            d = int(d)
    elif rounding == "fraction":
        d = x * 12
    elif rounding == "strict":
        raise Exception("Using strict rounding, not an exact number of pennies.")
    else:
        raise Exception("Not a correct rounding specification: %s." % rounding)
    return (l, s, d)
