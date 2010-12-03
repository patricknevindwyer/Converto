import types
"""

Rearrangement:

    measurement.core
        -> core classes (Measurement, UnitCombiner)
    measurement.bases
        -> all of the base unit types (Length, Time, etc)
    measurement.conversions
        -> how all of the base units relate
    measurement.(length | time | area | whatever).(si | imperial | fantasy | esoteric | whatever)
        -> instantiations of units
        
    measurement
        -> imports (in order)
        -> bases, conversions
    
    by hand import of instantiated units
"""
from measurement.core import UnitCombiner, Measurement
from measurement.bases import *
import measurement.conversion



