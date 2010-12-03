'''
Created on Dec 3, 2010

@author: patricknevindwyer

Julian years and higher measurements 
'''
from measurement.bases import Time
from measurement.time.gregorian import months, decades

years = Time(
    toBaseUnit = 86400.0 * 365.25,
    fromBaseUnit = 0.000000031688088,
    suffixes = ("year", 'years')
)

years.setSequenceUnits(up = decades, down = months)