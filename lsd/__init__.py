from decimal import Decimal


def pounds_and_new_pence(l, s, d):
    l = Decimal(l)
    s = Decimal(s)
    d = Decimal(d)
    return l + s / 20 + d / 240


def pounds_shillings_and_pence(x):
    l = int(x)
    x = x - l
    s = int(x * 20)
    x = x * 20 - s
    d = int(round(x * 12))
    return (l, s, d)
