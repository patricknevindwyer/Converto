'''
Created on Nov 4, 2010

@author: patricknevindwyer
'''
from converto import Measurement

class Length(Measurement):
    """
    Description of length and distance. The base unit for Length is the METER.
    
    * all measurements are stored in the base unit (in this case METERS)
    * all measurements are stored as floats
    * When doing operative math with Numeric arguments, the scale value is first
        converted into the scaled type. So when doing:
            
            (2 * miles) * 5
        
        The scaled miles value (2) is converted into the local scaled type (miles)
        multiplied, and then stored again in the base type. This keeps with the
        semantic meaning of the current unit, and avoids mathematical gaffes.
        
    TODO: Add unit and unit relations
    TODO: group suffix into a dict with short/long single/plural
    TODO: fix the op and rop methods to not point to the same code (rop will have different semantics)
    """
    pass
            
miles = Length(
    unit = 'mile',
    toBaseUnit = 1609.344,
    fromBaseUnit = 0.000621371192,
    suffixSingle = 'mile',
    suffixPlural = 'miles'
)

feet = Length(
    unit = 'foot',
    toBaseUnit = 0.3048,
    fromBaseUnit = 3.2808399,
    suffixSingle = 'foot',
    suffixPlural = 'feet' 
)

kilometers = Length(
    unit = 'kilometer',
    toBaseUnit = 1000.0,
    fromBaseUnit = 0.001,
    suffixSingle = 'kilometer',
    suffixPlural = 'kilometers'
)

meters = Length(
    unit = 'meter',
    toBaseUnit = 1.0,
    fromBaseUnit = 1.0,
    suffixSingle = 'meter',
    suffixPlural = 'meters'
)

centimeters = Length(
    unit = 'centimeter',
    toBaseUnit = 0.01,
    fromBaseUnit = 100.0,
    suffixSingle = 'centimeter',
    suffixPlural = 'centimeters'
)

furlongs = Length(
    unit = 'furlong',
    toBaseUnit = 201.16800,
    fromBaseUnit = 0.00497096954,
    suffixSingle = 'furlong',
    suffixPlural = 'furlongs'
)