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
    """
        Convert a fractional number of shillings into
        a number of old pence. E.g. 0.375 converts to
        4.5, only if the granularity is hapennies or farthings.
        If the desired granularity is pence this will fail.
    """
    d = x * 12 * k
    if d != int(d):
        raise ConversionError(granularity)
    if k == 1:
        d = int(d)
    else:
        d = float(d / k)
    return d
