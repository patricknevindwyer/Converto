'''
Created on Nov 23, 2010

@author: patricknevindwyer

Definitions for Metric/SI Length measurements. All SI measurement units
are linked for up/down scaling. These measurements stretch from yoctometers
to yottameters.
'''
from measurement.bases import Length

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