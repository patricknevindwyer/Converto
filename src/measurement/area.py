'''
Created on Nov 20, 2010

@author: patricknevindwyer
'''
from measurement.bases import Area 

square_meters = Area(
    toBaseUnit = 1.0,
    fromBaseUnit = 1.0,
    suffixes = ('square meter', 'square meters')
)

square_feet = Area(
    toBaseUnit = 0.09290304,
    fromBaseUnit = 10.7639104,
    suffixes = ('square foot', 'square feet')
)