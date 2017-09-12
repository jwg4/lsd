from .error import ConversionError, ArgumentError


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
        raise ArgumentError("granularity", granularity)


def _strict_rounding(x, k, granularity):
    d = x * 12 * k
    if d != int(d):
        raise ConversionError(granularity)
    if k == 1:
        d = int(d)
    else:
        d = float(d / k)
    return d
