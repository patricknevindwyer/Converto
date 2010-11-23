This changelog is an approximate catalog of syntax changes, new features, and bug fixes.

Changes
=======
_2010.11.23_
*	Created UnitCombiner class to handle dimensional conversions, rather than per-class definitions
*	added UnitCombiner handlers
	*	register_mul	-	commutative multiplication of units
	*	register_div	-	non-commutative division of units
	*	register_pow	-	exponent scaled dimensional shift
	
_2010.11.20_
*	Added dimensional_mul and dimensional_pow to Measurement base class
*	Added Area Measurement
*	Length supports dimensional_mul to create Area

_2010.11.19_

*	Added rich comparisons to all Measurement types
*	Added [Temperature](http://en.wikipedia.org/wiki/Temperature) measurements
*	Modified Measurement class to use numeric literal OR functions for base/local scale conversions

_2010.11.18_
	
*	Added left and right shifting support for left hand operands:
	
		# convert to kilometers
		(1000 * meters) << 1
		
		# convert to feet
		(3 * miles) >> 1

*	Added __storage__ measurements for SI and IEC prefixes, up to yotta/yobi bytes