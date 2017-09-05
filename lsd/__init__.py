from decimal import Decimal

def pounds_and_new_pence(l, s, d):
    l = Decimal(l)
    s = Decimal(s)
    d = Decimal(d)
    return l + s / 20 + d / 240