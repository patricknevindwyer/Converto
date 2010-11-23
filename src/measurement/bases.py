'''
Created on Nov 23, 2010

@author: patricknevindwyer

Summary
=======

The measurement.bases module contains all of the common base classes for defining
measurements. These are not instantiations of classes, just individual class types.

Classes
=======

The following base classes are defined. Each listed class is categorized by it's base
unit (in parenthesis) and a possible brief description.

-    Area (_square_meters_)
    -    2 dimensional spatial measurement
-    Temperature (_kelvin_)
    -    Heat / Temperature measurement
-    Length (_meters_)
    -    1 dimensional spatial measurement
-    Storage (_bytes_)
    -    Byte based digital storage measurement
-    Time (_seconds_)
    -    Time measurement
'''

from measurement import Measurement

class Area(Measurement):
    """
    _base quantity_ - SQUARE METER
    """
    pass

class Temperature(Measurement):
    """
    _base quantity_ - KELVIN    
    """
    pass

class Length(Measurement):
    """
    _base quantity_ - METER
    """
    pass

class Storage(Measurement):
    """
    _base quantity_ - BYTE        
    """
    pass

class Time(Measurement):
    """
    _base quantity_ - SECONDS
    """
    pass