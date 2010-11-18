This changelog is an approximate catalog of syntax changes, new features, and bug fixes.

Changes
=======
_2010.11.18_
	
	*	Added left and right shifting support for left hand operands:
	
		# convert to kilometers
		(1000 * meters) << 1
		
		# convert to feet
		(3 * miles) >> 1