import types

class ConversionError(Exception):
    
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg
    
class MeasurementError(Exception):
    
    def __init__(self, msg):
        self.msg = msg
    
    def __str_(self):
        return self.msg

class UnitCombiner(object):
    """
    The UnitCombiner class stores logic and class based patterns for how different unit
    types combine together through various operations to form new units. This logic is
    used by the base Measurement class to determine when and how to combine units of different
    types.
    
    An instance of UnitCombiner is bound to the measurement.* namespace, such that all unit
    combinations can be registered to a common instance:
        
        from measurement import unitCombiner as uc
        
        # This combination is now available to any measurements and code that reference
        # the measurement package
        uc.register_mul(Length, Length, Area)
        
    Class information can be used to define new patterns and combinations at will; these patterns
    will hold true for all instances and variations of the classes. So, for instance, the Length
    base class could define:
    
        unitCombiner.register_mul(Length, Length, Area)
        unitCombiner.register_mul(Length, Area, Volume)
        
    These two definitions make it possible to dimensionally shift a length into an Area (1d to 2d),
    and multiple Lengths or a Length and an Area into a Volume (1d x3 or 1d x 2d to 3d). The multiplication
    definitions are commutative, so the following two definitions are redundant:
        
        unitCombiner.register_mul(Length, Area, Volume)
        unitCombiner.register_mul(Area, Length, Volume)
    
    When determining how to combine to types, the multiplication code searches both combinations to find
    and appropriate pattern.
    
    The division definitions are non-commutative, so the following definition:
        
        unitCombiner.register_div(Area, Length, Length)
    
    defines how to divide an Area by a Length to create a Length. This pattern does not apply when dividing
    a Length by an Area (no applicable unit).
    
    The exponentiation logic (*_pow) defines patterns for raising units to different powers. Each base type
    can be given any number of distinct valid powers:
    
        unitCombiner.register_pow(Length, 2, Area)
        unitCombiner.register_pow(Length, 3, Volume)
    """
    def __init__(self):
        self._dim_mul = {}
        self._dim_pow = {}
        self._dim_div = {}
    
    def register_mul(self, left_class, right_class, result_class):
        """
        Create a new multiplication pattern using two base Measurement classes. Multiplication definitions
        are commutative; only a single combination of two distinct Measurement classes need be defined, the
        multiplication logic will attempt to find an applicable pattern using both Left/Right and Right/Left
        combinations.
            
            # define how two lengths combine into an Area
            unitCombiner.register_mul(Length, Length, Area)
        
        """
        pass
    
    def register_div(self, lop, rop, res):
        """
        Create a new division pattern using two base Measurement classes. Division definitions are
        non-commutative;
            
            Area / Length
        
        is not the same as:
            
            Length / Area
        
        For that reason definitions of unit combinations must be explicit for the desired syntactic ordering
        of Measurements:
            
            # Convert an Area into a Length by division using Length
            unitCombiner.register_div(Area, Length, Length)
            
            # Convert a Volume to a Length by division using Area
            unitCombiner.register_div(Volume, Area, Length)
        """
        pass
    
    def register_pow(self, lop, scale):
        """
        """
        pass

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
        
    TODO: fix the op and rop methods to not point to the same code (rop will have different semantics)
    TODO: Throw exceptions for unsupport ops
    """
    
    def __init__(self, *kargs, **kwargs):
        
        if 'copy' in kwargs:
            # copy an existing object
            copy = kwargs['copy']
            self.toBaseUnit = copy.toBaseUnit
            self.fromBaseUnit = copy.fromBaseUnit
            self.suffixes = copy.suffixes
            if 'scale' in kwargs:          
                self.scale = kwargs['scale']
            else:
                self.scale = copy.scale
                
            self.sequenceUnits = copy.sequenceUnits
            
        else:
            # create a new length object
            self.toBaseUnit = kwargs['toBaseUnit']
            self.fromBaseUnit = kwargs['fromBaseUnit']
            self.suffixes = kwargs['suffixes']
            self.scale = None
            self.sequenceUnits = {'up': None, 'down': None}
            
    
    def setSequenceUnits(self, **kwargs):
        """
        Set the sequence units for this measurement corresponding to a shift up
        or down the unit granularity.
        """
        parts = ['up', 'down']
        for part in parts:
            if part in kwargs:
                self.sequenceUnits[part] = kwargs[part]

    def __str__(self):
        
        if self.scale is None:
            return self.suffixPlural
        else:
            
            displayScale = self.toLocal()
            suffix = self.suffixes[-1]
            
            if self.scale == 1.0 or self.scale == -1.0:
                suffix = self.suffixes[0]
                
            return "%0.2f %s" % (displayScale, suffix)
    
    def reconstruct(self, *kargs, **kwargs):
        return self.__class__(*kargs, **kwargs)
    
    """
    Dimensional Conversion methods. Each subclass of Measurement can define how to combine
    different scaled measurements into new objects. For instance, the Length class defines
    how two Lengths combine into an Area. The Area class defines how Area and Length combine
    into Volume.
    
    If a class does not define a means of combining two measurements, it can return None to
    trigger a ConversionError. Likewise, if a class has no means of dimensionally shifting
    values, it can skip these methods all together.
    """
    def dimensional_mul(self, other):
        raise ConversionError("%s doesn't support dimensional multiplication" % (self.__class__))
    
    def dimensional_pow(self, other):
        raise ConversionError("%s doesn't support dimensional exponentiation" % (self.__class__))
    
    """
    COMPARISONS
        
        Comparators using the base unit. None-comparable units will generate a MeasurementError.
    """
    def __typeCompare(self, other):
        """
        Basic class comparison. This throws a MeasurementError if the two classes are not compatible.
        """
        if not isinstance(other, self.__class__):
            raise MeasurementError("Objects are not of compatible Measurement type")
    
    def __lt__(self, other):
        """
        self < other
        """
        self.__typeCompare(other)
        return self.scale < other.scale
    
    def __le__(self, other):
        """
        self <= other
        """
        self.__typeCompare(other)
        return self.scale <= other.scale
    
    def __gt__(self, other):
        """
        self > other
        """
        self.__typeCompare(other)
        return self.scale > other.scale
    
    def __ge__(self, other):
        """
        self >= other
        """
        self.__typeCompare(other)
        return self.scale >= other.scale

    def __eq__(self, other):
        """
        self == other
        """
        self.__typeCompare(other)
        return self.scale == other.scale

    def __ne__(self, other):
        """
        self != other
        """
        self.__typeCompare(other)
        return self.scale != other.scale
    
    """
    COMMON BASE CONVERSION
        
        These methods are used when converting values to and from the base unit. The conversion method can be a number or
        a function.
    """
    def toLocal(self, scale=None):
        """
        Convert the scale value to the local measurement scale. The fromBaseUnit value can be a literal
        or a function. If the scale value is not directly specified the self.scale value is used.
        """
        
        # determine our conversion base number
        toVal = scale
        if toVal is None:
            toVal = self.scale
            
        # determine the conversion method
        if type(self.fromBaseUnit) == types.FunctionType:
            return self.fromBaseUnit(toVal)
        elif type(self.fromBaseUnit) == types.FloatType:
            return toVal * self.fromBaseUnit
        else:
            raise ConversionError("Invalid type specified for converting from the base unit (%s): %s" % (",".join(self.suffixes), type(self.fromBaseUnit)))
    
    def toBase(self, scale=None):
        """
        Convert the scale value to the base measurement unit. The toBaseUnit value can be a literal
        or a function. If the scale value is not directly specified the self.scale value is used.
        """
        
        # determine our conversion base number
        fromVal = scale
        if fromVal is None:
            fromVal = self.scale
        
        # determine the conversion method
        if type(self.toBaseUnit) == types.FunctionType:
            return self.toBaseUnit(fromVal)
        elif type(self.toBaseUnit) == types.FloatType:
            return fromVal * self.toBaseUnit
        else:
            raise ConversionError("Invalid type specified for converting to the base unit (%s): %s" % (",".join(self.suffixes), type(self.toBaseUnit)))
    
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
        return self.toLocal()
    
    def __getattr__(self, name):
        if name == 'size':
            return self.toLocal()
        else:
            raise AttributeError
        
    """
    SHIFTING
        
        Shifting causes a unit change within the sequence spectrum
    """
    
    def __lshift__(self, other):
        """
        Shift our Measurement Unit the given distance along it's sequence, using a unit iteration. This function
        captures the following literate syntax:
            
            l = 400 * meters
            l = l << 1
            
        Here we're jumping up one unit of distance to kilometers. If a unit of the sequence
        doesn't exist, say:
            
            l = 100 * meters
            l = l << 10
            
        Then we return the last plausible unit in the sequence.
        """
        
        if type(other) == types.IntType:
            
            # sanity check
            if other == 0:
                return self
            
            # start it up
            resMeasurement = self.reconstruct(copy=self)
            
            for shift in range(0, other):
                
                # stop when we can't shift up any higher
                if resMeasurement.sequenceUnits['up'] is None:
                    break
                
                # shift to the next unit
                resMeasurement = self.reconstruct(copy = resMeasurement.sequenceUnits['up'], scale = self.scale)
            
            return resMeasurement
        else:
            return None
    
    def __rshift__(self, other):
        """
        Shift our Measurement Unit the given distance along it's sequence, using a unit iteration. This function
        captures the following literate syntax:
            
            l = 1 * kilometers
            l = l >> 1
            
        Here we're jumping down one unit of distance to meters. If a unit of the sequence
        doesn't exist, say:
            
            l = 100 * feet
            l = l >> 10
            
        Then we return the last plausible unit in the sequence.
        """
        if type(other) == types.IntType:
            
            # sanity check
            if other == 0:
                return self
            
            # start it up
            resMeasurement = self.reconstruct(copy=self)
            
            for shift in range(0, other):
                
                # stop when we can't shift up any higher
                if resMeasurement.sequenceUnits['down'] is None:
                    break
                
                # shift to the next unit
                resMeasurement = self.reconstruct(copy = resMeasurement.sequenceUnits['down'], scale = self.scale)
            
            return resMeasurement
        else:
            return None
    
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
                return self.reconstruct(copy = self, scale = self.toBase(other))
            else:
                # modify existing scaled measurement
                return self.reconstruct(copy = self, scale =  self.toBase(self.toLocal() / other) )
        else:
            
            if isinstance(other, self.__class__) and self.scale is not None and other.scale is not None:
                # common units in scaled division results in a unitless number, ie: 10 miles divided
                # by 2 miles is the unitless number 5. The resuting scale is determined by the
                # left hand basetype
                return (self.scale / other.scale)
            elif self.scale is not None and other.scale is not None:
                # create a compound unit, but we need to reduce the num/denom
                
                # handled by UnitCombiner singleton
#                return CompoundMeasurement(
#                    measurements = [
#                        self.reconstruct(copy = self, scale = self.scale / other.scale),
#                        other.reconstruct(copy = other, scale = 1)
#                    ]
#                )
                pass
            
            elif self.scale is not None and other.scale is None:
                
                # handled by UnitCombiner singleton
#                
#                # create a simple compound unit
#                return CompoundMeasurement(
#                    measurements = [
#                        self.reconstruct(copy = self, scale = self.scale),
#                        other.reconstruct(copy = other, scale = 1)
#                    ]
#                )
                pass

    
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
            return self.reconstruct(copy = self, scale = self.toBase(self.toLocal() - other) )
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
            return self.reconstruct(copy = self, scale = self.toBase(self.toLocal() + other))
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
                return self.reconstruct(copy = self, scale = self.toBase(float(other)))
            else:
                # actual measurement multiplication. All measurement math happens in
                # the local unit scale
                return self.reconstruct(copy = self, scale = self.toBase(self.toLocal() * other) )
            
        else:
            if isinstance(other, self.__class__) and other.scale == None and self.scale is not None:
                # this is a scale conversion using our scale and the other base type
                return self.reconstruct(copy = other, scale = self.scale)
            elif isinstance(other, self.__class__) and other.scale is not None and self.scale is None:
                # this is a scale conversion using the other scale and our base type
                return self.reconstruct(copy = self, scale = other.scale)
            elif other.scale is not None and self.scale is not None:
                # unit combination and dimensional increase
                retVal = self.dimensional_mul(other)
                if retVal is None:
                    raise ConversionError( "Invalid dimensional multiplication between %s and %s" % (self.__class__, other.__class__) )
                else:
                    return retVal