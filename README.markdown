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
	
	
Conversions
===========

In it's current rudimentary form Converto supports the following units:

*	Length
	-	miles
	-	feet
	-	kilometers
	-	meters
	-	centimeters
	-	furlongs

*	Time
	-	seconds
	-	minutes
	-	hours
	-	days


Examples
========

Create a basic measurement
	
	from converto.length import miles
	
	d = 5 * miles
	
	# 5.00 miles
	print d

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
	
Roadmap
=======

* Comparisons and other operators
* Single vs plural units, unit abbreviations
* Add more unit types (volume, area)
* Add compound units and multi-unit math
* Add chained units (convert a length into miles _and_ feet, or a time into days, hours, minutes, and seconds)
* Examples, syntax changes


