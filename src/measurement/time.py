'''
Created on Nov 4, 2010

@author: patricknevindwyer
'''
from measurement import Measurement

class Time(Measurement):
    """
    The base for Time is seconds.
    """
    pass

seconds = Time(
    unit = 'second',
    toBaseUnit = 1.0,
    fromBaseUnit = 1.0,
    suffixes = ('second', 'seconds')
)

minutes = Time(
    unit = 'minute',
    toBaseUnit = 60.0,
    fromBaseUnit = 0.0166666667,
    suffixes = ('minute', 'minutes')
)

hours = Time(
    unit = 'hour',
    toBaseUnit = 3600.0,
    fromBaseUnit = 0.000277777778,
    suffixes = ('hour', 'hours')
)

days = Time(
    unit = 'day',
    toBaseUnit = 86400.0,
    fromBaseUnit = 0.000011574074074,
    suffixes = ('day', 'days')
)

days.setSequenceUnits(down = hours)
hours.setSequenceUnits(up = days, down = minutes)
minutes.setSequenceUnits(up = hours, down = seconds)
seconds.setSequenceUnits(up = minutes)
