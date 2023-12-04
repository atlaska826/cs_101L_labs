import math


def total(values):
    return float(sum(values))


def average(values):
    if len(values) == 0:
        return math.nan
    return float(sum(values) / len(values))


def median(values):
    if len(values) == 0:
        raise ValueError
    else:
        values = sorted(values)
        index = int(len(values) / 2)
        if len(values) % 2 == 0:
            return (values[index] + values[index - 1]) / 2
        else:
            return values[index]
