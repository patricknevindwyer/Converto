'''
Created on Nov 4, 2010

@author: patricknevindwyer
'''
from converto import Measurement
from converto.area import square_meters

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
        
    TODO: fix the op and rop methods to not point to the same code (rop will have different semantics)
    """
    def dimensional_mul(self, other):
        """
            Length * Length -> Area
            Length * Area -> Volume
            Length * Time -> Speed
        """
        
        if isinstance(other, self.__class__):
            # Length * Length
            return square_meters * (self.scale * other.scale)
        else:
            return None
            
###
# IMPERIAL UNITS
###
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

###
# METRIC UNITS
###

yottameters = Length(
    toBaseUnit = 1000000000000000000000000.0,
    fromBaseUnit = 0.000000000000000000000001,
    suffixes = ('yottameter', 'yottameters')
)

zettameters = Length(
    toBaseUnit = 1000000000000000000000.0,
    fromBaseUnit = 0.000000000000000000001,
    suffixes = ('zettameter', 'zettameters')
)

exameters = Length(
    toBaseUnit = 1000000000000000000.0,
    fromBaseUnit = 0.000000000000000001,
    suffixes = ('exameter', 'exameters')
)

petameters = Length(
    toBaseUnit = 1000000000000000.0,
    fromBaseUnit = 0.000000000000001,
    suffixes = ('petameter', 'petameters')
)

terameters = Length(
    toBaseUnit = 1000000000000.0,
    fromBaseUnit = 0.000000000001,
    suffixes = ('terameter', 'terameters')
)

gigameters = Length(
    toBaseUnit = 1000000000.0,
    fromBaseUnit = 0.000000001,
    suffixes = ('gigameter', 'gigameters')
)

megameters = Length(
    toBaseUnit = 1000000.0,
    fromBaseUnit = 0.000001,
    suffixes = ('megameter', 'megameters')
)

kilometers = Length(
    toBaseUnit = 1000.0,
    fromBaseUnit = 0.001,
    suffixes = ('kilometer', 'kilometers')
)

hectometers = Length(
    toBaseUnit = 100.0,
    fromBaseUnit = 0.01,
    suffixes = ('hectometer', 'hectometers')
)

decameters = Length(
    toBaseUnit = 10.0,
    fromBaseUnit = 0.1,
    suffixes = ('decameter', 'decameters')
)

meters = Length(
    toBaseUnit = 1.0,
    fromBaseUnit = 1.0,
    suffixes = ('meter', 'meters')
)

decimeters = Length(
    toBaseUnit = 0.1,
    fromBaseUnit = 10.0,
    suffixes = ('decimeter', 'decimeters')
)

centimeters = Length(
    toBaseUnit = 0.01,
    fromBaseUnit = 100.0,
    suffixes = ('centimeter', 'centimeters')
)

millimeters = Length(
    toBaseUnit = 0.001,
    fromBaseUnit = 1000.0,
    suffixes = ('millimeter', 'millimeters')
)

micrometers = Length(
    toBaseUnit = 0.000001,
    fromBaseUnit = 1000000.0,
    suffixes = ('micrometer', 'micrometers')
)

nanometers = Length(
    toBaseUnit = 0.000000001,
    fromBaseUnit = 1000000000.0,
    suffixes = ('nanometer', 'nanometers')
)

picometers = Length(
    toBaseUnit = 0.000000000001,
    fromBaseUnit = 1000000000000.0,
    suffixes = ('picometer', 'picometers')
)

femtometers = Length(
    toBaseUnit = 0.000000000000001,
    fromBaseUnit = 1000000000000000.0,
    suffixes = ('femtometer', 'femtometers')
)

attometers = Length(
    toBaseUnit = 0.000000000000000001,
    fromBaseUnit = 1000000000000000000.0,
    suffixes = ('attometer', 'attometers')
)

zeptometers = Length(
    toBaseUnit = 0.000000000000000000001,
    fromBaseUnit = 1000000000000000000000.0,
    suffixes = ('zeptometer', 'zeptometers')
)

yoctometers = Length(
    toBaseUnit = 0.000000000000000000000001,
    fromBaseUnit = 1000000000000000000000000.0,
    suffixes = ('yoctometer', 'yoctometers')
)

yottameters.setSequenceUnits(down = zettameters)
zettameters.setSequenceUnits(up = yottameters, down = exameters)
exameters.setSequenceUnits(up = zettameters, down = petameters)
petameters.setSequenceUnits(up = exameters, down = terameters)
terameters.setSequenceUnits(up = petameters, down = gigameters)
gigameters.setSequenceUnits(up = terameters, down = megameters)
megameters.setSequenceUnits(up = gigameters, down = kilometers)
kilometers.setSequenceUnits(up = megameters, down = hectometers)
hectometers.setSequenceUnits(up = kilometers, down = decameters)
decameters.setSequenceUnits(up = hectometers, down = meters)
meters.setSequenceUnits(up = decameters, down = decimeters)
decimeters.setSequenceUnits(up = meters, down = centimeters)
centimeters.setSequenceUnits(up = decimeters, down = millimeters)
millimeters.setSequenceUnits(up = centimeters, down = micrometers)
micrometers.setSequenceUnits(up = millimeters, down = nanometers)
nanometers.setSequenceUnits(up = micrometers, down = picometers)
picometers.setSequenceUnits(up = nanometers, down = femtometers)
femtometers.setSequenceUnits(up = picometers, down = attometers)
attometers.setSequenceUnits(up = femtometers, down = zeptometers)
zeptometers.setSequenceUnits(up = attometers, down = yoctometers)
yoctometers.setSequenceUnits(up = zeptometers)

###
# ESOTERIC UNITS
###
furlongs = Length(
    unit = 'furlong',
    toBaseUnit = 201.16800,
    fromBaseUnit = 0.00497096954,
    suffixes = ('furlong', 'furlongs')
)