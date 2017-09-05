from decimal import Decimal


def pounds_and_new_pence(l, s, d):
    l = Decimal(l)
    s = Decimal(s)
    d = Decimal(d)
    return l + s / 20 + d / 240


def _get_granularity_multiplier(granularity):
    if granularity == "penny":
        return 1
    elif granularity == "hapenny":
        return 2
    elif granularity == "farthing":
        return 4
    else:
        raise Exception("Not a correct granularity specification: %s." % granularity)


def _strict_rounding(x, k):
    d = x * 12 * k
    if d != int(d):
        raise Exception("Using strict rounding, not an exact number of pennies.")
    if k == 1:
        d = int(d)
    else:
        d = float(d / k)
    return d


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
        d = _strict_rounding(x, k)
    else:
        raise Exception("Not a correct rounding specification: %s." % rounding)
    return (l, s, d)
