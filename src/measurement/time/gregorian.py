'''
Created on Dec 3, 2010

@author: patricknevindwyer

Gregorian breakdown of Time - any time breakdown dependent upon quantization of days, hours, and minutes.
'''
from measurement.bases import Time
from measurement.time.si import seconds

minutes = Time(
    unit = 'minute',
    toBaseUnit = 60.0,
    fromBaseUnit = 0.0166666667,
    suffixes = ('minute', 'minutes')
)

hours = Time(
    unit = 'hour',
    toBaseUnit = 3600.0,
    fromBaseUnit = 0.000277777778,
    suffixes = ('hour', 'hours')
)

days = Time(
    unit = 'day',
    toBaseUnit = 86400.0,
    fromBaseUnit = 0.000011574074074,
    suffixes = ('day', 'days')
)

weeks = Time(
    toBaseUnit = 86400.0 * 7.0,
    fromBaseUnit = 0.000001653439153,
    suffixes = ('week', 'weeks')
)

fortnights = Time(
    toBaseUnit = 86400.0 * 14.0,
    fromBaseUnit = 0.000000826719577,
    suffixes = ('fortnight', 'fortnights')
)

"""
Month definitions follow a standard month, and then breakout months
for specific month lengths, as well as a leap_february.
"""
months = Time(
    toBaseUnit = 86400.0 * 31.0,
    fromBaseUnit = 0.000000373357228,
    suffixes = ('month', 'months')
)

short_months = Time(
    toBaseUnit = 86400.0 * 30.0,
    fromBaseUnit = 0.000000385802469,
    suffixes = ('month', 'months')
)

month_february = Time(
    toBaseUnit = 86400.0 * 28,
    fromBaseUnit = 0.000000413359788,
    suffixes = ('month', 'months')
)

month_leap_february = Time(
    toBaseUnit = 86400.0 * 29.0,
    fromBaseUnit = 0.000000399106003,
    suffixes = ('month', 'months')
)

month_january = months
month_march = months
month_april = short_months
month_may = months
month_june = short_months
month_july = months
month_august = months
month_september = short_months
month_october = months
month_november = short_months
month_december = months


quarters = Time(
    toBaseUnit = 86400.0 * 31.0 * 3,
    fromBaseUnit = 0.000000124452409,
    suffixes = ('quarter', 'quarters')
)

years = Time(
    toBaseUnit = 86400.0 * 365.2425,
    fromBaseUnit = 0.000000031688739,
    suffixes = ('year', 'years')
)

decades = Time(
    toBaseUnit = 86400.0 * 365.2425 * 10.0,
    fromBaseUnit = 0.000000003168874,
    suffixes = ('decade', 'decades')
)

centuries = Time(
    toBaseUnit = 86400.0 * 356.2425 * 100.0,
    fromBaseUnit = 0.000000000316887,
    suffixes = ('century', 'centuries')
)

millennia = Time(
    toBaseUnit = 86400.0 * 365.2425 * 1000.0,
    fromBaseUnit = 0.000000000031689,
    suffixes = ('millennium', 'millennia')
)

millennia.setSequenceUnits(down = centuries)
centuries.setSequenceUnits(up = millennia, down = decades)
decades.setSequenceUnits(up = centuries, down = years)
years.setSequenceUnits(up = decades, down = months)
quarters.setSequenceUnits(up = years, down = months)

months.setSequenceUnits(up = years, down = days)
short_months.setSequenceUnits(up = years, down = days)
month_february.setSequenceUnits(up = years, down = days)
month_leap_february.setSequenceUnits(up = years, down = days)

fortnights.setSequenceUnits(up = months, down = weeks)
weeks.setSequenceUnits(up = months, down = days)
days.setSequenceUnits(up = weeks, down = hours)
hours.setSequenceUnits(up = days, down = minutes)
minutes.setSequenceUnits(up = hours, down = seconds)
