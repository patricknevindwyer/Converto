'''
Created on Nov 23, 2010

@author: patricknevindwyer

All conversions are grouped by the target Measurement, so, for instance, all conversions
that result in Area are grouped together.
'''
from measurement.bases import Area, Length
from measurement.core import unitCombiner as uc

from measurement.area import square_meters
from measurement.length.si import meters


"""
AREA
"""
uc.register_mul(Length, Length, square_meters)
uc.register_pow(Length, 2, square_meters)

"""
Length
"""
uc.register_div(Area, Length, meters)