class ConversionError(Exception):
    def __init__(self, granularity, decimal=False):
        self.granularity = granularity
        self.decimal = decimal

    def __str__(self):
        return "Using strict rounding, not an exact number of %s." % (self.unit, )

    @property
    def unit(self):
        if self.granularity == "penny":
            if self.decimal:
                return "new pence"
            else:
                return "pennies"
        elif self.granularity == "hapenny":
            return "ha'pennies"
        elif self.granularity == "farthing":
            return "farthings"
        elif self.granularity == "halfpenny":
            return "half pence"