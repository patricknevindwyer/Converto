'''
Created on Dec 3, 2010

@author: patricknevindwyer

SI breakdown of time, based upon the second
'''
from measurement.bases import Time

yoctoseconds = Time(
   toBaseUnit = 1000000000000000000000000.0,
   fromBaseUnit = 0.000000000000000000000001,
   suffixes = ('yoctosecond', 'yoctoseconds')
)

zeptoseconds = Time(
   toBaseUnit = 1000000000000000000000.0,
   fromBaseUnit = 0.000000000000000000001,
   suffixes = ('zeptosecond', 'zeptoseconds')
)

attoseconds = Time(
   toBaseUnit = 1000000000000000000.0,
   fromBaseUnit = 0.000000000000000001,
   suffixes = ('attosecond', 'attoseconds')
)

femtoseconds = Time(
   toBaseUnit = 1000000000000000.0,
   fromBaseUnit = 0.000000000000001,
   suffixes = ('femtosecond', 'femtoseconds')
)

picoseconds = Time(
   toBaseUnit = 1000000000000.0,
   fromBaseUnit = 0.000000000001,
   suffixes = ('picosecond', 'picoseconds')
)

nanoseconds = Time(
   toBaseUnit = 1000000000.0,
   fromBaseUnit = 0.000000001,
   suffixes = ('nanosecond', 'nanoseconds')
)

microseconds = Time(
   toBaseUnit = 1000000.0,
   fromBaseUnit = 0.000001,
   suffixes = ('microsecond', 'microseconds')
)

milliseconds = Time(
   toBaseUnit = 1000.0,
   fromBaseUnit = 0.001,
   suffixes = ('millisecond', 'milliseconds')
)

centiseconds = Time(
   toBaseUnit = 100.0,
   fromBaseUnit = 0.01,
   suffixes = ('centisecond', 'centiseconds')
)

deciseconds = Time(
   toBaseUnit = 10.0,
   fromBaseUnit = 0.1,
   suffixes = ('decisecond', 'deciseconds')
)

seconds = Time(
   toBaseUnit = 1.0,
   fromBaseUnit = 1.0,
   suffixes = ('second', 'seconds')
)

decaseconds = Time(
   toBaseUnit = 0.1,
   fromBaseUnit = 10.0,
   suffixes = ('decasecond', 'decaseconds')
)

hectoseconds = Time(
   toBaseUnit = 0.01,
   fromBaseUnit = 100.0,
   suffixes = ('hectosecond', 'hectoseconds')
)

kiloseconds = Time(
   toBaseUnit = 0.001,
   fromBaseUnit = 1000.0,
   suffixes = ('kilosecond', 'kiloseconds')
)

megaseconds = Time(
   toBaseUnit = 0.000001,
   fromBaseUnit = 1000000.0,
   suffixes = ('megasecond', 'megaseconds')
)

gigaseconds = Time(
   toBaseUnit = 0.000000001,
   fromBaseUnit = 1000000000.0,
   suffixes = ('gigasecond', 'gigaseconds')
)

teraseconds = Time(
   toBaseUnit = 0.000000000001,
   fromBaseUnit = 1000000000000.0,
   suffixes = ('terasecond', 'teraseconds')
)

petaseconds = Time(
   toBaseUnit = 0.000000000000001,
   fromBaseUnit = 1000000000000000.0,
   suffixes = ('petasecond', 'petaseconds')
)

exaseconds = Time(
   toBaseUnit = 0.000000000000000001,
   fromBaseUnit = 1000000000000000000.0,
   suffixes = ('exasecond', 'exaseconds')
)

zettaseconds = Time(
   toBaseUnit = 0.000000000000000000001,
   fromBaseUnit = 1000000000000000000000.0,
   suffixes = ('zettasecond', 'zettaseconds')
)

yottaseconds = Time(
   toBaseUnit = 0.000000000000000000000001,
   fromBaseUnit = 1000000000000000000000000.0,
   suffixes = ('yottasecond', 'yottaseconds')
)

yoctoseconds.setSequenceUnits(up = zeptoseconds)
zeptoseconds.setSequenceUnits(up = attoseconds, down = yoctoseconds)
attoseconds.setSequenceUnits(up = femtoseconds, down = zeptoseconds)
femtoseconds.setSequenceUnits(up = picoseconds, down = attoseconds)
picoseconds.setSequenceUnits(up = nanoseconds, down = femtoseconds)
nanoseconds.setSequenceUnits(up = microseconds, down = picoseconds)
microseconds.setSequenceUnits(up = milliseconds, down = nanoseconds)
milliseconds.setSequenceUnits(up = centiseconds, down = microseconds)
centiseconds.setSequenceUnits(up = deciseconds, down = milliseconds)
deciseconds.setSequenceUnits(up = seconds, down = centiseconds)
seconds.setSequenceUnits(up = decaseconds, down = deciseconds)
decaseconds.setSequenceUnits(up = hectoseconds, down = seconds)
hectoseconds.setSequenceUnits(up = kiloseconds, down = decaseconds)
kiloseconds.setSequenceUnits(up = megaseconds, down = hectoseconds)
megaseconds.setSequenceUnits(up = gigaseconds, down = kiloseconds)
gigaseconds.setSequenceUnits(up = teraseconds, down = megaseconds)
teraseconds.setSequenceUnits(up = petaseconds, down = gigaseconds)
petaseconds.setSequenceUnits(up = exaseconds, down = teraseconds)
exaseconds.setSequenceUnits(up = zettaseconds, down = petaseconds)
zettaseconds.setSequenceUnits(up = yottaseconds, down = exaseconds)
yottaseconds.setSequenceUnits(down = zettaseconds)