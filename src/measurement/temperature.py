'''
Created on Nov 19, 2010

@author: patricknevindwyer
'''
from measurement.bases import Temperature

"""
The Temperature measurements incorporate a range of temperature types, each of which uses
a formula to convert to and from the base temperature unit of Kelvin
"""

kelvin = Temperature(
    toBaseUnit = 1.0,
    fromBaseUnit = 1.0,
    suffixes = ('K',)
)

celsius = Temperature(
    toBaseUnit = lambda c: c + 273.15,
    fromBaseUnit = lambda k: k - 273.15,
    suffixes = ('C',) 
)

fahrenheit = Temperature(
    toBaseUnit = lambda f: (f + 459.67) * (5.0 / 9.0),
    fromBaseUnit = lambda k: (k * (9.0 / 5.0)) - 459.67,
    suffixes = ('F',)
)

rankine = Temperature(
    toBaseUnit = lambda r: r * (5.0 / 9.0),
    fromBaseUnit = lambda k: k * (9.0 / 5.0),
    suffixes = ('R',)
)

delisle = Temperature(
    toBaseUnit = lambda d: 373.15 - (d * (2.0 / 3.0)),
    fromBaseUnit = lambda k: (373.15 - k) * (3.0 / 2.0),
    suffixes = ('D',)
)

newton = Temperature(
    toBaseUnit = lambda n: n * (100.0 / 33.0) + 273.15,
    fromBaseUnit = lambda k: (k - 273.15) * (33.0 / 100.0),
    suffixes = ('N',)
)

reaumur = Temperature(
    toBaseUnit = lambda re: re * (5.0 / 4.0) + 273.15,
    fromBaseUnit = lambda k: (k - 273.15) * (4.0 / 5.0),
    suffixes = ('Re',)
)

romer = Temperature(
    toBaseUnit = lambda ro: (ro - 7.5) * (40.0 / 21.0) + 273.15,
    fromBaseUnit = lambda k: (k - 273.15) * (21.0 / 40.0) + 7.5,
    suffixes = ('Ro',)
)