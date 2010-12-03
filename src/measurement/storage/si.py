'''
Created on Dec 3, 2010

@author: patricknevindwyer

SI (powers of 10) Storage
'''
from measurement.bases import Storage

bytes = Storage(
    toBaseUnit = 1.0,
    fromBaseUnit = 1.0,
    suffixes = ('b',)
)

kilobytes = Storage(
    toBaseUnit = 1000.0,
    fromBaseUnit = 0.001,
    suffixes = ('kB',)
)

megabytes = Storage(
    toBaseUnit = 1000000.0,
    fromBaseUnit = 0.000001,
    suffixes = ('MB',)
)

gigabytes = Storage(
    toBaseUnit = 1000000000.0,
    fromBaseUnit = 0.000000001,
    suffixes = ('GB',)
)

terabytes = Storage(
    toBaseUnit = 1000000000000.0,
    fromBaseUnit = 0.000000000001,
    suffixes = ('TB',)
)

petabytes = Storage(
    toBaseUnit = 1000000000000000.0,
    fromBaseUnit = 0.000000000000001,
    suffixes = ('PB',)
)

exabytes = Storage(
    toBaseUnit = 1000000000000000000.0,
    fromBaseUnit = 0.000000000000000001,
    suffixes = ('EB',)
)

zettabytes = Storage(
    toBaseUnit = 1000000000000000000000.0,
    fromBaseUnit = 0.000000000000000000001,
    suffixes = ('ZB',)
)

yottabytes = Storage(
    toBaseUnit = 1000000000000000000000000.0,
    fromBaseUnit = 0.000000000000000000000001,
    suffixes = ('YB',)
)

yottabytes.setSequenceUnits(down = zettabytes)
zettabytes.setSequenceUnits(up = yottabytes, down = exabytes)
exabytes.setSequenceUnits(up = zettabytes, down = petabytes)
petabytes.setSequenceUnits(up = exabytes, down = terabytes)
terabytes.setSequenceUnits(up = petabytes, down = gigabytes)
gigabytes.setSequenceUnits(up = terabytes, down = megabytes)
megabytes.setSequenceUnits(up = gigabytes, down = kilobytes)
kilobytes.setSequenceUnits(up = megabytes, down = bytes)