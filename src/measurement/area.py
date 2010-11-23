'''
Created on Nov 20, 2010

@author: patricknevindwyer
'''
from converto import Measurement

class Area(Measurement):
    """
    Description of 2 dimensional area. The base unit for Area is the METER.
    
    * all measurements are stored in the base unit (in this case METERS)
    * all measurements are stored as floats
    * When doing operative math with Numeric arguments, the scale value is first
        converted into the scaled type. So when doing:
            
            (2 * miles) * 5
        
        The scaled miles value (2) is converted into the local scaled type (miles)
        multiplied, and then stored again in the base type. This keeps with the
        semantic meaning of the current unit, and avoids mathematical gaffes.
        
    TODO: fix the op and rop methods to not point to the same code (rop will have different semantics)
    """
    pass

square_meters = Area(
    toBaseUnit = 1.0,
    fromBaseUnit = 1.0,
    suffixes = ('square meter', 'square meters')
)

square_feet = Area(
    toBaseUnit = 0.09290304,
    fromBaseUnit = 10.7639104,
    suffixes = ('square foot', 'square feet')
)