'''
Created on Nov 23, 2010

@author: patricknevindwyer
'''
from measurement.bases import *
from measurement import unitCombiner as uc

from measurement.area import square_meters
from measurement.length import meters

uc.register_mul(Length, Length, square_meters)
uc.register_div(Area, Length, meters)