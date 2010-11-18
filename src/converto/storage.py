'''
Created on Nov 18, 2010

@author: patricknevindwyer
'''
from converto import Measurement

class Storage(Measurement):
    """
    Description of computer storage. The base unit for Length is the BYTE.
    
    * all measurements are stored in the base unit (in this case BYTES)
    * all measurements are stored as floats
    * When doing operative math with Numeric arguments, the scale value is first
        converted into the scaled type. So when doing:
            
            (2 * miles) * 5
        
        The scaled miles value (2) is converted into the local scaled type (miles)
        multiplied, and then stored again in the base type. This keeps with the
        semantic meaning of the current unit, and avoids mathematical gaffes.
        
    """
    pass

"""
The Storage measurements incorporate both the SI decimal prefixes (measuring in powers of 10),
and the IEC binary prefixes (measuring in powers of 2).
"""

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

kibibytes = Storage(
    toBaseUnit = 1024.0,
    fromBaseUnit = 1.0 / 1024.0,
    suffixes = ('KiB',)
)


megabytes = Storage(
    toBaseUnit = 1000000.0,
    fromBaseUnit = 0.000001,
    suffixes = ('MB',)
)

mebibytes = Storage(
    toBaseUnit = 1024.0 ** 2,
    fromBaseUnit = 1 / (1024.0 * 1024.0),
    suffixes = ('MiB',)  
)


gigabytes = Storage(
    toBaseUnit = 1000000000.0,
    fromBaseUnit = 0.000000001,
    suffixes = ('GB',)
)

gibibytes = Storage(
    toBaseUnit = 1024.0 ** 3,
    fromBaseUnit = 1.0 / (1024.0 ** 3),
    suffixes = ('GiB',)
)


terabytes = Storage(
    toBaseUnit = 1000000000000.0,
    fromBaseUnit = 0.000000000001,
    suffixes = ('TB',)
)

tebibytes = Storage(
    toBaseUnit = 1024.0 ** 4,
    fromBaseUnit = 1.0 / (1024.0 ** 4),
    suffixes = ('TiB',)
)


petabytes = Storage(
    toBaseUnit = 1000000000000000.0,
    fromBaseUnit = 0.000000000000001,
    suffixes = ('PB',)
)

pebibytes = Storage(
    toBaseUnit = 1024.0 ** 5,
    fromBaseUnit = 1.0 / (1024.0 ** 5),
    suffixes = ('PiB',)
)


exabytes = Storage(
    toBaseUnit = 1000000000000000000.0,
    fromBaseUnit = 0.000000000000000001,
    suffixes = ('EB',)
)

exbibytes = Storage(
    toBaseUnit = 1024.0 ** 6,
    fromBaseUnit = 1.0 / (1024.0 ** 6),
    suffixes = ('EiB',)
)


zettabytes = Storage(
    toBaseUnit = 1000000000000000000000.0,
    fromBaseUnit = 0.000000000000000000001,
    suffixes = ('ZB',)
)

zebibytes = Storage(
    toBaseUnit = 1024 ** 7,
    fromBaseUnit = 1.0 / (1024.0 ** 7),
    suffixes = ('ZiB',)
)


yottabytes = Storage(
    toBaseUnit = 1000000000000000000000000.0,
    fromBaseUnit = 0.000000000000000000000001,
    suffixes = ('YB',)
)

yobibytes = Storage(
    toBaseUnit = 1024.0 ** 8,
    fromBaseUnit = 1.0 / (1024.0 ** 8),
    suffixes = ('YiB',)
)

# SI relationships
yottabytes.setSequenceUnits(down = zettabytes)
zettabytes.setSequenceUnits(up = yottabytes, down = exabytes)
exabytes.setSequenceUnits(up = zettabytes, down = petabytes)
petabytes.setSequenceUnits(up = exabytes, down = terabytes)
terabytes.setSequenceUnits(up = petabytes, down = gigabytes)
gigabytes.setSequenceUnits(up = terabytes, down = megabytes)
megabytes.setSequenceUnits(up = gigabytes, down = kilobytes)
kilobytes.setSequenceUnits(up = megabytes, down = bytes)

# IEC relationships
yobibytes.setSequenceUnits(down = zebibytes)
zebibytes.setSequenceUnits(up = yobibytes, down = exbibytes)
exbibytes.setSequenceUnits(up = zebibytes, down = pebibytes)
pebibytes.setSequenceUnits(up = exbibytes, down = tebibytes)
tebibytes.setSequenceUnits(up = pebibytes, down = gibibytes)
gibibytes.setSequenceUnits(up = tebibytes, down = mebibytes)
mebibytes.setSequenceUnits(up = gibibytes, down = kibibytes)
kibibytes.setSequenceUnits(up = mebibytes, down = bytes)