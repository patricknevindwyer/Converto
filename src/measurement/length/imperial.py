'''
Created on Nov 23, 2010

@author: patricknevindwyer

Definitions for Imperial Length measurement units. 
'''
from measurement.bases import Length

miles = Length(
    toBaseUnit = 1609.344,
    fromBaseUnit = 0.000621371192,
    suffixes = ('mile', 'miles')
)

feet = Length(
    toBaseUnit = 0.3048,
    fromBaseUnit = 3.2808399,
    suffixes = ('foot','feet') 
)

miles.setSequenceUnits(down = feet)
feet.setSequenceUnits(up = miles)
