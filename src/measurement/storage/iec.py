'''
Created on Dec 3, 2010

@author: patricknevindwyer

IEC (powers of 2) Storage
'''
from measurement.bases import Storage
from measurement.storage.si import bytes

kibibytes = Storage(
    toBaseUnit = 1024.0,
    fromBaseUnit = 1.0 / 1024.0,
    suffixes = ('KiB',)
)

mebibytes = Storage(
    toBaseUnit = 1024.0 ** 2,
    fromBaseUnit = 1 / (1024.0 * 1024.0),
    suffixes = ('MiB',)  
)

gibibytes = Storage(
    toBaseUnit = 1024.0 ** 3,
    fromBaseUnit = 1.0 / (1024.0 ** 3),
    suffixes = ('GiB',)
)

tebibytes = Storage(
    toBaseUnit = 1024.0 ** 4,
    fromBaseUnit = 1.0 / (1024.0 ** 4),
    suffixes = ('TiB',)
)

pebibytes = Storage(
    toBaseUnit = 1024.0 ** 5,
    fromBaseUnit = 1.0 / (1024.0 ** 5),
    suffixes = ('PiB',)
)

exbibytes = Storage(
    toBaseUnit = 1024.0 ** 6,
    fromBaseUnit = 1.0 / (1024.0 ** 6),
    suffixes = ('EiB',)
)

zebibytes = Storage(
    toBaseUnit = 1024 ** 7,
    fromBaseUnit = 1.0 / (1024.0 ** 7),
    suffixes = ('ZiB',)
)

yobibytes = Storage(
    toBaseUnit = 1024.0 ** 8,
    fromBaseUnit = 1.0 / (1024.0 ** 8),
    suffixes = ('YiB',)
)

# IEC relationships
yobibytes.setSequenceUnits(down = zebibytes)
zebibytes.setSequenceUnits(up = yobibytes, down = exbibytes)
exbibytes.setSequenceUnits(up = zebibytes, down = pebibytes)
pebibytes.setSequenceUnits(up = exbibytes, down = tebibytes)
tebibytes.setSequenceUnits(up = pebibytes, down = gibibytes)
gibibytes.setSequenceUnits(up = tebibytes, down = mebibytes)
mebibytes.setSequenceUnits(up = gibibytes, down = kibibytes)
kibibytes.setSequenceUnits(up = mebibytes, down = bytes)
