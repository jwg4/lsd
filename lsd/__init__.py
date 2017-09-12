from decimal import Decimal


def pounds_and_new_pence(l, s, d, rounding="nearest", granularity="halfpenny"):
    l = Decimal(l)
    s = Decimal(s)
    d = Decimal(d)
    exact = l + s / 20 + d / 240
    multiplier = _get_granularity_multiplier(granularity)
    if rounding == "nearest":
        return round(exact * multiplier, 2) / Decimal(multiplier)
    if rounding == "strict":
        pence = exact * multiplier * 100
        if pence != int(pence):
            raise Exception("Using strict rounding, not an exact number of new pence.")
        return pence / (100 * multiplier)
    elif rounding == "fraction":
        return exact
    else:
        raise Exception("Not a correct rounding specification: %s." % rounding)


def _get_granularity_multiplier(granularity):
    if granularity == "penny":
        return 1
    elif granularity == "hapenny":
        return 2
    elif granularity == "halfpenny":
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
