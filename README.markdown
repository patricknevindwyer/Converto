Welcome to Converto (pronounced convert-o, not conver-to); a simple measurement and 
unit conversion library for Python. This library is primarily an experiment in abusing
operator overloading in classes to provide as literate a syntax as possible for moving
between common measurement units. 

Literate Conversion
===================

This library is predicated on the idea that it's better to run across this in the middle
of a source file:

	# convert our running distance to centimeters
	distance = 5 * miles * centimeters

Than this:
	
	# convert our running distance to centimeters
	distance = 5 * 160934.4

Or to work with time using sane combinations:
	
	# determine how many days it's been since the last update
	elapsedSeconds = 1000000
	elapsedDays = elapsedSeconds * seconds * days
	
Converto can also help avoid mistakes when mixing different units in the same code:
	
	# compare the different distances we collected
	k = 15 * kilometers
	m = 10 * miles
	
	if m > k:
		# do something
	
Conversions
===========

In it's current rudimentary form Converto supports the following units:

*	Length
	-	miles
	-	feet
	-	furlongs
	-	Standard [SI prefixes](http://en.wikipedia.org/wiki/Metre#SI_prefixed_forms_of_metre "SI Prefixes"), from yoctometers (10 ^ -24) to yottameters (10 ^ 24)

*	Time
	-	seconds
	-	minutes
	-	hours
	-	days

*	[Storage](http://en.wikipedia.org/wiki/Byte#Unit_symbol_or_abbreviation "Byte Multiples")
	-	SI prefixes (kilo, mega, giga, tera, peta, exa, zetta, yotta)
	-	IEC prefixes (kibi, mebi, gibi, tebi, pebi, exbi, zebi, yobi)
	
*	[Temperature](http://en.wikipedia.org/wiki/Temperature "Temperature")
	-	Fahrenheit
	-	Celsius
	-	Kelvin
	-	Rankine
	-	Delisle
	-	Newton
	-	Reaumur
	-	Romer
	
*	Area
	-	square_meters
	-	square_feet
	
Examples
========

Create a basic measurement
	
	from converto.length import miles
	
	d = 5 * miles
	
	# 5.00 miles
	print d

Compare measurements in different units
	
	from converto.length import miles, kilometers
	
	m = 10 * miles
	k = 15 * kilometers
	
	if m > k:
		print "That's a lot of miles"
	
Modify a measurement
	
	from converto.time import *
	
	t = 10 * seconds * 6
	
	# 60.00 seconds
	print t

Convert between measurements
	
	from converto.length import meters, miles
	
	lap = 400 * meters
	run = lap * 10 * miles
	
	# 2.49 miles
	print run

Get the value of a measurement. It's important to note that while __len()__ and the __size__ attribute can both be
used to get the value of a measurement, the __len()__ will always be rounded to an integer value. This is fine in
some cases, but dangerous in others where the decimal portion of a measurement is meaningful.
	
	from converto.time import days, seconds
	from converto.length import miles, meters
	
	d = 1 * days * seconds
	
	# 86,400
	print len(d)
	
	l = 1 * miles * meters
	
	# 1609.344
	print l.size
	
Basic measurement math
	
	from converto.length import feet, centimeters
	
	s = ( 1 * feet ) - ( 10 * centimeters )
	
	# 0.67 feet
	print s
	
Shift between common measurements. The number shifted is not directly related to scale, but to the common sequence
of units. Hence, shifting from _meters_ to _nanometers_ is 5 steps (meter > decimeter > centimeter > millimeter >
micrometer > nanometer) not 9 (1 nanometer is 10 ^ -9 meters)
	
	from converto.length import *
	
	d = 5 * meters
	
	# convert to kilometers
	km = d << 3
	
	# convert to nanometers
	nm = d >> 5
	
Determine actual storage of a 1 terabyte harddrive:
	
	from converto.storage import *
	
	size = 1 * terabytes
	actual = size * tebibytes
	
	# 0.91 TiB
	print actual
	
Move between measurement dimensions:
	
	from converto.length import *
	from converto.area import *
	
	# determine size of an area by it's lengths
	w = 1 * furlongs
	h = 23 * centimeters
	
	# determine the size in square feet (498.03 square feet)
	a = (w * h) * square_feet
	
Roadmap
=======

*	add __pow__ method to Measurements
	*	add dimensional_pow to Measurements
*	Volume Measurement
	* dimensional_* for Length, Area, and Volume relationships
*	Add other dimensional shifts
	*	division
	*	roots
*	Measurement relationships
	* 	area x length == volume
	*	distance x time == speed
	*	speed x time == acceleration
	*	length and exponents
	*	dimensional singleton to define combinations and result base measurements, rather than per-class overloading? Both?
		*	Transitive mul, dimensioned pow, non-transitive div
*	unit tests
*	other operators
	*	indexing as conversion/mapping
	*	and/or/xor
	*	power
	*	i* ops (iadd, isub, etc)
	*	divmod
	*	binary ops
	*	hash
	*	repr
	*	slicing
*	add ConversionError and propogate it through the code to catch problems
*	scaledmeasurement <op> scaledmeasurement code path
*	Single vs plural units, unit abbreviations
*	Add compound units and multi-unit math via dimensional relationships
*	Add chained units (convert a length into miles _and_ feet, or a time into days, hours, minutes, and seconds)
*	Examples, syntax changes
*	Add other measurement units
	*	improve time
	*	force
	*	weight
	*	mass
	*	speed
	*	acceleration
	*	pressure
	*	torque