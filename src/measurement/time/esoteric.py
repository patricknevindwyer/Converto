'''
Created on Dec 3, 2010

@author: patricknevindwyer
'''
from measurement.bases import Time
from measurement.time.gregorian import months, years

common_years = Time(
    toBaseUnit = 86400.0 * 365.0,
    fromBaseUnit = 0.000000031709792,
    suffixes = ('year', 'years')
)

leap_years = Time(
    toBaseUnit = 86400.0 * 366.0,
    fromBaseUnit = 0.000000031623153,
    suffixes = ('year', 'years')
)

tropical_years = Time(
    toBaseUnit = 86400.0 * 365.24219,
    fromBaseUnit = 0.000000031688765,
    suffixes = ('year', 'years')
)

olympiad = Time(
    toBaseUnit = 86400.0 * 365.0 * 4.0,
    fromBaseUnit = 0.000000007927448,
    suffixes = ('olympiad')
)

lustrum = Time(
    toBaseUnit = 86400.0 * 365.0 * 5.0,
    fromBaseUnit = 0.000000006341958,
    suffixes = ('lustrum')
)

indiction = Time(
    toBaseUnit = 86400.0 * 365.0 * 15.0,
    fromBaseUnit = 0.000000002113986,
    suffixes = ('indiction')
)

jubilee = Time(
    toBaseUnit = 86400.0 * 365.0 * 50.0,
    fromBaseUnit = 0.000000000634196,
    suffixes = ('jubilee')
)

jubilee.setSequenceUnits(down = years)
indiction.setSequenceUnits(down = years)
lustrum.setSequenceUnits(down = years)
olympiad.setSequenceUnits(down = years)
common_years.setSequenceUnits(down = months)
tropical_years.setSequenceUnits(down = months)
leap_years.setSequenceUnits(down = months)