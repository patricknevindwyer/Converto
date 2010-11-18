'''
Created on Nov 4, 2010

@author: patricknevindwyer
'''
from converto import Measurement

class Time(Measurement):
    """
    The base for Time is seconds.
    """
    pass

seconds = Time(
    unit = 'second',
    toBaseUnit = 1.0,
    fromBaseUnit = 1.0,
    suffixSingle = 'seconds',
    suffixPlural = 'seconds'
)

minutes = Time(
    unit = 'minute',
    toBaseUnit = 60.0,
    fromBaseUnit = 0.0166666667,
    suffixSingle = 'minute',
    suffixPlural = 'minutes'
)

hours = Time(
    unit = 'hour',
    toBaseUnit = 3600.0,
    fromBaseUnit = 0.000277777778,
    suffixSingle = 'hour',
    suffixPlural = 'hours'
)

days = Time(
    unit = 'day',
    toBaseUnit = 86400.0,
    fromBaseUnit = 0.000011574074074,
    suffixSingle = 'day',
    suffixPlural = 'days'
)