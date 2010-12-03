'''
Created on Dec 3, 2010

@author: patricknevindwyer

SI measurements of Area
'''
from measurement.bases import Area 

square_meters = Area(
    toBaseUnit = 1.0,
    fromBaseUnit = 1.0,
    suffixes = ('square meter', 'square meters')
)