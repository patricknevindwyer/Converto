import types

class CompoundMeasurement(object):
    """
    A compound measurement using multiple units, for instance 5 miles / hour. Certain combinations
    of compound measurements can be done to derive new figures.
    
        * Compound (op) Compound
        * Compound (op) Numeric
        * Compound (op) Scaled Measurement
        
    When the compound unit is created it is always simplified to have a denominator of 1
    
    Example 1 - Pace to Time
    ------------------------
    
    Establish a pace (time / distance):
        
        pace = 8 minutes / mile
        
    Mulitply this pace by a distance to get a time (unit cancellation):
        
        time = pace * 5 miles
    
    Time is now in minutes (simple scaled measurement):
        
        str(time) # 40 minutes
        
    Example 2 - Time to Pace
    ------------------------
    
    Establish a distance and time:
        
        race = 5 km / 24 minutes
    
    Multiply this distance and time by a time and distance to get a pace
        
        pace = race * (minutes / mile)
    
    The pace is now in root units of time / distance (unit inversion):
        
        str(pace) # 7.### minutes / mile
    """
    
    def __init__(self, *kargs, **kwargs):
        
        self.measurements = kwargs['measurements']

    def __mul__(self, other):
        """
        Check for all kinds of modifications and operations that can happen
        """
        
        if other.__class__ == self.measurements[-1].__class__:
            # unit cancellation, the result of this is the scale of the other (in it's local form)
            # times the scale of the numerator
            print "unit cancellation"
            numerator = self.measurements[0]
            
            return numerator.reconstruct(copy = numerator, scale = numerator.scale * (other.scale * other.fromBaseUnit))
        
class Measurement(object):
    """
    Description of a measurement.
    
    * all measurements are stored in the base unit
    * all measurements are stored as floats
    * When doing operative math with Numeric arguments, the scale value is first
        converted into the scaled type. So when doing:
            
            (2 * miles) * 5
        
        The scaled miles value (2) is converted into the local scaled type (miles)
        multiplied, and then stored again in the base type. This keeps with the
        semantic meaning of the current unit, and avoids mathematical gaffes.
        
    TODO: Add unit and unit relations
    TODO: group suffix into a dict with short/long single/plural
    TODO: fix the op and rop methods to not point to the same code (rop will have different semantics)
    TODO: Throw exceptions for unsupport ops
    """
    
    def __init__(self, *kargs, **kwargs):
        
        if 'copy' in kwargs:
            # copy an existing object
            copy = kwargs['copy']
            self.toBaseUnit = copy.toBaseUnit
            self.fromBaseUnit = copy.fromBaseUnit
            self.suffixSingle = copy.suffixSingle
            self.suffixPlural = copy.suffixPlural
            self.unit = copy.unit            
            self.scale = kwargs['scale']
            
            
        else:
            # create a new length object
            self.toBaseUnit = kwargs['toBaseUnit']
            self.fromBaseUnit = kwargs['fromBaseUnit']
            self.suffixSingle = kwargs['suffixSingle']
            self.suffixPlural = kwargs['suffixPlural']
            self.unit = kwargs['unit']
            self.scale = None
    
    def __str__(self):
        
        if self.scale is None:
            return self.suffixPlural
        else:
            
            displayScale = self.scale * self.fromBaseUnit
            suffix = self.suffixPlural
            
            if self.scale == 1.0 or self.scale == -1.0:
                suffix = self.suffixSingle
                
            return "%0.2f %s" % (displayScale, suffix)
    
    def reconstruct(self, *kargs, **kwargs):
        return self.__class__(*kargs, **kwargs)
    
    """
    SCALE LOOKUP
    
        These methods capture scale lookup and other basic metadata inquiry. 
    """
    def __len__(self):
        """
        Return the scaled size in this unit type. This isn't the preferred method
        of retrieving the scale of this measurement, as it rounds all values to
        integers
        """
        return self.scale * self.fromBaseUnit
    
    def __getattr__(self, name):
        if name == 'size':
            return self.scale * self.fromBaseUnit
        else:
            raise AttributeError
    """
    DIVISION
    
        For measurement types, division has quite a few modes
        
        1. scaled measurement / numeric  ==  Division of scaled measurement
        2. numeric / scaled measurement  ==  Division of implicit scaled measurement
        3. numeric / basetype            ==  Conversion of numeric type into scaled measurement
        #4. scaledmeasurement / basetype  ==  Unit combination (ie: miles / hours == milesperhour)
        #5. basetype / basetype           ==  Unscaled unit combination (ie: mph)
        6. scaled measurement / scaled measurement (same types)  ==  Division of common distances into raw value (non-unit number)
        #7. scaled measurement / scaled measurement (diff types)  ==  Unit combination 

    """
    def __rdiv__(self, other):
        return self.__div__(other)
    
    def __div__(self, other):
        """
        Self is the left term, other is the right
        """
        
        if type(other) == types.IntType or type(other) == types.FloatType:
            if self.scale is None:
                # create new scaled measurement
                return self.reconstruct(copy = self, scale = other * self.toBaseUnit)
            else:
                # modify existing scaled measurement
                return self.reconstruct(copy = self, scale = ((self.scale * self.fromBaseUnit) / other) * self.toBaseUnit)
        else:
            
            if isinstance(other, self.__class__) and self.scale is not None and other.scale is not None:
                # common units in scaled division results in a unitless number, ie: 10 miles divided
                # by 2 miles is the unitless number 5. The resuting scale is determined by the
                # left hand basetype
                return (self.scale / other.scale)
            elif self.scale is not None and other.scale is not None:
                # create a compound unit, but we need to reduce the num/denom
                return CompoundMeasurement(
                    measurements = [
                        self.reconstruct(copy = self, scale = self.scale / other.scale),
                        other.reconstruct(copy = other, scale = 1)
                    ]
                )
            elif self.scale is not None and other.scale is None:
                # create a simple compound unit
                return CompoundMeasurement(
                    measurements = [
                        self.reconstruct(copy = self, scale = self.scale),
                        other.reconstruct(copy = other, scale = 1)
                    ]
                )

    
    """
    SUBTRACTION
    
        For measurement types, subtraction has a few modes
        
        1. Numeric - scaled measurement             ==  Conversion of Numeric to basetype and subtraction
        2. scaled measurement - Numeric             ==  Conversion of Numeric to basetype and subtraction
        3. scaled measurement - scaled measurement  ==  conversion to left basetype and subtraction
    """
    def __rsub__(self, other):
        return self.__sub__(other)
    
    def __sub__(self, other):
        """
        Self is the left operand, other is the right
        """
        
        if type(other) == types.IntType or type(other) == types.FloatType:
            return self.reconstruct(copy = self, scale = ((self.scale * self.fromBaseUnit) - other) * self.toBaseUnit)
        else:
            
            if isinstance(other, self.__class__) and self.scale is not None and other.scale is not None:
                return self.reconstruct(copy = self, scale = self.scale - other.scale)

    
    """
    ADDITION
        
        For measurement types, addition has a few modes:
        
        1. Numeric + scaled measurement             ==  Conversion of Numeric to basetype and addition
        2. scaled measurement + Numeric             ==  Conversion of Numeric to basetype and addition
        3. scaled measurement + scaled measurement  ==  conversion to left basetype and addition
    """
    def __radd__(self, other):
        return self.__add__(other)
    
    def __add__(self, other):
        """
        Self is the left operand, other is the right
        """
        
        if type(other) == types.IntType or type(other) == types.FloatType:
            
            # add length of the current base type
            return self.reconstruct(copy = self, scale = ((self.scale * self.fromBaseUnit) + other) * self.toBaseUnit)
        else:
            
            if isinstance(other, self.__class__) and self.scale is not None and other.scale is not None:
                
                # this conversion works regardless of basetype, as all basetypes store in the
                # root unit
                return self.reconstruct(copy = self, scale = self.scale + other.scale)

    
    """
    MULTIPLICATION
    
        For measurement types, multiplication has a few modes:
        
        1. Numeric * basetype             ==  scaled measurement
        2. basetype * Numeric             ==  scaled measurement
        3. Numeric * scaled measurement   ==  scaled measurement
        4. scaled measurement * Numeric   ==  scaled measurement
        5. basetype * scaled measurement  ==  conversion to alternate basetype
        6. scaled measurement * basetype  ==  conversion to alternate basetype
    """
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __mul__(self, other):
        """
        Give this length object a scale. The scale value in this case must
        be a numeric type
        """
        
        if type(other) == types.IntType or type(other) == types.FloatType:
            
            if self.scale is None:
                # creating a new scaled measurement
                return self.reconstruct(copy = self, scale = float(other) * self.toBaseUnit)
            else:
                # actual measurement multiplication. All measurement math happens in
                # the local unit scale
                return self.reconstruct(copy = self, scale = (self.scale * self.fromBaseUnit * other) * self.toBaseUnit)
            
        else:
            if isinstance(other, self.__class__) and other.scale == None and self.scale is not None:
                # this is a scale conversion using our scale and the other base type
                return self.reconstruct(copy = other, scale = self.scale)
            elif isinstance(other, self.__class__) and other.scale is not None and self.scale is None:
                # this is a scale conversion using the other scale and our base type
                return self.reconstruct(copy = self, scale = other.scale)