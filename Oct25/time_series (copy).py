'''1. Write a Pandas program to create 
a) Datetime object for Jan 15 2012.
b) Specific date and time of 9:20 pm.
c) Local date and time.
d) A date without time.
e) Current date.
f) Time from a datetime.
g) Current local time.
Click me to see the sample solution'''

import datetime
from datetime import datetime
print("Datetime object for Jan 11 2012:")
print(datetime(2012, 1, 11))
print("\nSpecific date and time of 9:20 pm") 
print(datetime(2011, 1, 11, 21, 20))
print("\nLocal date and time:")
print(datetime.now())
print("\nA date without time: ")
print(datetime.date(datetime(2012, 5, 22)))
print("\nCurrent date:")
print(datetime.now().date())
print("\nTime from a datetime:")
print(datetime.time(datetime(2012, 12, 15, 18, 12)))
print("\nCurrent local time:") 
print(datetime.now().time())

'''2. Write a Pandas program to create 
a) a specific date using timestamp.
b) date and time using timestamp.
c) a time adds in the current local date using timestamp.
d) current date and time using timestamp.
Click me to see the sample solution'''

import pandas as pd
#from datetime import datetime
print("\nA specific date using timestamp:")
print(pd.Timestamp('2016-11-10'))
print("\nDate and time using timestamp:")
print(pd.Timestamp('2012-05-03 11:30'))
print("\nA time adds in the current local date using timestamp:")
print(pd.Timestamp('11:30'))
print("\nCurrent date and time using timestamp:")
print(pd.Timestamp("now"))

'''3. Write a Pandas program to create a date from a given year, month, day and another date from a given string formats. 
Click me to see the sample solution'''

from datetime import datetime
date1 = datetime(year=2020, month=12, day=25)
print("Date from a given year, month, day:")
print(date1)
from dateutil import parser
date2 = parser.parse("1st of January, 2021")
print("\nDate from a given string formats:")
print(date2)

'''4. Write a Pandas program to print the day after and before a specified date. Also print the days between two given dates. 
Click me to see the sample solution'''

import pandas as pd
import datetime
from datetime import datetime, date
today = datetime(2012, 10, 30)
print("Current date:", today)
tomorrow = today + pd.Timedelta(days=1)
print("Tomorrow:", tomorrow)
yesterday = today - pd.Timedelta(days=1)
print("Yesterday:", yesterday)
date1 = datetime(2016, 8, 2)
date2 = datetime(2016, 7, 19)
print("\nDifference between two dates: ",(date1 - date2))

'''5. Write a Pandas program to create a time-series with two index labels and random values. Also print the type of the index. 
Click me to see the sample solution'''

import pandas as pd
import numpy as np
import datetime
from datetime import datetime, date
dates = [datetime(2011, 9, 1), datetime(2011, 9, 2)]
print("Time-series with two index labels:")
time_series = pd.Series(np.random.randn(2), dates)
print(time_series)
print("\nType of the index:")
print(type(time_series.index))

'''6. Write a Pandas program to create a time-series from a given list of dates as strings. 
Click me to see the sample solution'''

import pandas as pd
import numpy as np
import datetime
from datetime import datetime, date 
dates = ['2014-08-01','2014-08-02','2014-08-03','2014-08-04']
time_series = pd.Series(np.random.randn(4), dates)
print(time_series)

'''7. Write a Pandas program to create a time series object that has time indexed data. Also select the dates of same year and select the dates between certain dates. 
Click me to see the sample solution'''

import pandas as pd
index = pd.DatetimeIndex(['2011-09-02', '2012-08-04',
                          '2015-09-03', '2010-08-04',
                          '2015-03-03', '2011-08-04',
                          '2015-04-03', '2012-08-04'])

s_dates = pd.Series([0, 1, 2, 3, 4, 5, 6, 7], index=index)

print("Time series object with indexed data:")
print(s_dates)
print("\nDates of same year:")
print(s_dates['2015'])
print("\nDates between 2012-01-01 and 2012-12-31")
print(s_dates['2012-01-01':'2012-12-31']) 

'''8. Write a Pandas program to create a date range using a startpoint date and a number of periods. 
Click me to see the sample solution'''

import pandas as pd
date_range = pd.date_range('2020-01-01', periods=45)
print("Date range of perods 45:")
print(date_range)

'''9. Write a Pandas program to create a whole month of dates in daily frequencies. Also find the maximum, minimum timestamp and indexs. 
Click me to see the sample solution'''

import pandas as pd
dates = pd.Series(pd.date_range('2020-12-01',periods=31, freq='D'))
print("Month of December 2020:")
print(dates)
dates = pd.Series(pd.date_range('2020-12-01',periods=31, freq='D'))
print("\nMaximum date: ", dates.max())
print("Minimum date: ", dates.min())
print("Maximum index: ", dates.idxmax())
print("Minimum index: ", dates.idxmin())

'''10. Write a Pandas program to create a time series using three months frequency. 
Click me to see the sample solution'''

import pandas as pd
time_series = pd.date_range('1/1/2021', periods = 36, freq='3M')
print("Time series using three months frequency:")
print(time_series) 

'''11. Write a Pandas program to create a sequence of durations increasing by an hour. 
Click me to see the sample solution'''

import pandas as pd
date_range = pd.timedelta_range(0, periods=49, freq='H')
print("Hourly range of perods 49:")
print(date_range)

'''12. Write a Pandas program to convert year and day of year into a single datetime column of a dataframe.
Click me to see the sample solution'''

import pandas as pd
data = {\
"year": [2002, 2003, 2015, 2018],
"day_of_the_year": [250, 365, 1, 140]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
df["combined"] = df["year"]*1000 + df["day_of_the_year"]
df["date"] = pd.to_datetime(df["combined"], format = "%Y%j")
print("\nNew DataFrame:")
print(df)

'''13. Write a Pandas program to create a series of Timestamps from a DataFrame of integer or string columns. Also create a series of Timestamps using specified columns. 
Click me to see the sample solution'''

import pandas as pd
df = pd.DataFrame({'year': [2018, 2019, 2020],
                   'month': [2, 3, 4],
                   'day': [4, 5, 6],
                   'hour': [2, 3, 4]})
print("Original dataframe:")
print(df)
result = pd.to_datetime(df)
print("\nSeries of Timestamps from the said dataframe:")
print(result)
print("\nSeries of Timestamps using specified columns:")
print(pd.to_datetime(df[['year', 'month', 'day']]))

'''14. Write a Pandas program to check if a day is a business day (weekday) or not. 
Click me to see the sample solution'''

import pandas as pd
def is_business_day(date):
    return bool(len(pd.bdate_range(date, date)))
print("Check busines day or not?")
print('2020-12-01: ',is_business_day('2020-12-01'))
print('2020-12-06: ',is_business_day('2020-12-06'))
print('2020-12-07: ',is_business_day('2020-12-07'))
print('2020-12-08: ',is_business_day('2020-12-08'))

'''15. Write a Pandas program to get a time series with the last working days of each month of a specific year. 
Click me to see the sample solution'''

import pandas as pd
s = pd.date_range('2021-01-01', periods=12, freq='BM')
df = pd.DataFrame(s, columns=['Date'])
print('last working days of each month of a specific year:')
print(df)

'''16. Write a Pandas program to create a time series combining hour and minute. 
Click me to see the sample solution'''

import pandas as pd
result = pd.timedelta_range(0, periods=30, freq="1H20T")
print("For a frequency of 1 hours 20 minutes, here we have combined the hour (H) and minute (T):\n")
print(result)

'''17. Write a Pandas program to convert unix/epoch time to a regular time stamp in UTC. Also convert the said timestamp in to a given time zone. 
Click me to see the sample solution'''

import pandas as pd
epoch_t = 1621132355
time_stamp = pd.to_datetime(epoch_t, unit='s')
# UTC (Coordinated Universal Time) is one of the well-known names of UTC+0 time zone which is 0h.
# By default, time series objects of pandas do not have an assigned time zone.
print("Regular time stamp in UTC:")
print(time_stamp)
print("\nConvert the said timestamp in to US/Pacific:")
print(time_stamp.tz_localize('UTC').tz_convert('US/Pacific'))
print("\nConvert the said timestamp in to Europe/Berlin:")
print(time_stamp.tz_localize('UTC').tz_convert('Europe/Berlin'))

'''18. Write a Pandas program to create a time series object with a time zone. 
Click me to see the sample solution'''

import pandas as pd
print("Timezone: Europe/Berlin:")
print("Using pytz:")
date_pytz = pd.Timestamp('2019-01-01', tz = 'Europe/Berlin')
print(date_pytz.tz)  
print("Using dateutil:")
date_util = pd.Timestamp('2019-01-01', tz = 'dateutil/Europe/Berlin')
print(date_util.tz)
print("\nUS/Pacific:")
print("Using pytz:")
date_pytz = pd.Timestamp('2019-01-01', tz = 'US/Pacific')
print(date_pytz.tz)  
print("Using dateutil:")
date_util = pd.Timestamp('2019-01-01', tz = 'dateutil/US/Pacific')
print(date_util.tz)

'''19. Write a Pandas program to remove the time zone information from a Time series data. 
Click me to see the sample solution'''

import pandas as pd
date1 = pd.Timestamp('2019-01-01', tz='Europe/Berlin')
date2 = pd.Timestamp('2019-01-01', tz='US/Pacific')
date3 = pd.Timestamp('2019-01-01', tz='US/Eastern')
print("Time series data with time zone:")
print(date1)
print(date2)
print(date3)
print("\nTime series data without time zone:")
print(date1.tz_localize(None))
print(date2.tz_localize(None))
print(date3.tz_localize(None))

'''20. Write a Pandas program to subtract two timestamps of same time zone or different time zone. 
Click me to see the sample solution'''

import pandas as pd
print("Subtract two timestamps of same time zone:")
date1 = pd.Timestamp('2019-03-01 12:00', tz='US/Eastern')
date2 = pd.Timestamp('2019-04-01 07:00', tz='US/Eastern')
print("Difference: ", (date2-date1))
print("\nSubtract two timestamps of different time zone:")
date1 = pd.Timestamp('2019-03-01 12:00', tz='US/Eastern')
date2 = pd.Timestamp('2019-03-01 07:00', tz='US/Pacific')
# Remove the time zone and do the subtraction
print("Difference: ", (date1.tz_localize(None) - date2.tz_localize(None)))

'''21. Write a Pandas program to calculate all Thursdays between two given days. 
Click me to see the sample solution'''

import pandas as pd
thursdays  = pd.date_range('2020-01-01', 
                           '2020-12-31', freq="W-THU")
print("All Thursdays between 2020-01-01 and 2020-12-31:\n")
print(thursdays.values)

'''22. Write a Pandas program to find the all the business quarterly begin and end dates of a specified year. 
Click me to see the sample solution'''

import pandas as pd
q_start_dates = pd.date_range('2020-01-01', '2020-12-31', freq='BQS-JUN')
q_end_dates = pd.date_range('2020-01-01', '2020-12-31', freq='BQ-JUN')
print("All the business quarterly begin dates of 2020:")
print(q_start_dates.values)
print("\nAll the business quarterly end dates of 2020:")
print(q_end_dates.values)

'''23. Write a Pandas program to generate sequences of fixed-frequency dates and time spans intervals. 
Click me to see the sample solution'''

import pandas as pd
print("Sequences of fixed-frequency dates and time spans (1 H):\n")
r1 = pd.date_range('2030-01-01', periods=10, freq='H')
print(r1)
print("\nSequences of fixed-frequency dates and time spans (3 H):\n")
r2 = pd.date_range('2030-01-01', periods=10, freq='3H')
print(r2)

'''24. Write a Pandas program to generate time series combining day and intraday offsets intervals. 
Click me to see the sample solution'''

import pandas as pd
dateset1 = pd.date_range('2029-01-01 00:00:00', periods=20, freq='3h10min')
print("Time series with frequency 3h10min:")
print(dateset1)
dateset2 = pd.date_range('2029-01-01 00:00:00', periods=20, freq='1D10min20U')
print("\nTime series with frequency 1 day 10 minutes and 20 microseconds:")
print(dateset2)

'''25. Write a Pandas program to extract the day name from a specified date. Add 2 days and 1 business day with the specified date. 
Click me to see the sample solution'''

import pandas as pd
newday = pd.Timestamp('2020-02-07')
print("First date:")
print(newday)
print("\nThe day name of the said date:")
print(newday.day_name())
print("\nAdd 2 days with the said date:")
newday1 = newday + pd.Timedelta('2 day')
print(newday1.day_name())
print("\nNext business day:")
nbday = newday + pd.offsets.BDay()
print(nbday.day_name())

'''26. Write a Pandas program to convert integer or float epoch times to Timestamp and DatetimeIndex. 
Click me to see the sample solution'''

import pandas as pd
dates1 = pd.to_datetime([1329806505, 129806505, 1249892905,
                1249979305, 1250065705], unit='s')
print("Convert integer or float epoch times to Timestamp and DatetimeIndex upto second:")
print(dates1)
print("\nConvert integer or float epoch times to Timestamp and DatetimeIndex upto milisecond:")
dates2 = pd.to_datetime([1249720105100, 1249720105200, 1249720105300,
                1249720105400, 1249720105500], unit='ms')
print(dates2)

'''27. Write a Pandas program to calculate one, two, three business day(s) from a specified date. Also find the next business month end from a specific date. 
Click me to see the sample solution'''

import pandas as pd
from pandas.tseries.offsets import *
import datetime
from datetime import datetime, date
dt = datetime(2020, 1, 4)
print("Specified date:")
print(dt)
print("\nOne business day from the said date:")
obday = dt + BusinessDay()
print(obday)
print("\nTwo business days from the said date:")
tbday = dt + 2 * BusinessDay()
print(tbday)
print("\nThree business days from the said date:")
thbday = dt + 3 * BusinessDay()
print(thbday)
print("\nNext business month end from the said date:")
nbday = dt + BMonthEnd()
print(nbday)

'''28. Write a Pandas program to create a period index represent all monthly boundaries of a given year. Also print start and end time for each period object in the said index. 
Click me to see the sample solution'''

import pandas as pd
import datetime
from datetime import datetime, date
sdt = datetime(2020, 1, 1)
edt = datetime(2020, 12, 31)
dateset = pd.period_range(sdt, edt, freq='M')
print("All monthly boundaries of a given year:")
print(dateset) 
print("\nStart and end time for each period object in the said index:")
for d in dateset: 
    print ("{0} {1}".format(d.start_time, d.end_time)) 

'''29. Write a Pandas program create a series with a PeriodIndex which represents all the calendar month periods in 2029 and 2031. Also print the values for all periods in 2030. 
Note: PeriodIndex is an immutable ndarray holding ordinal values indicating regular periods in time such as particular years, quarters, months, etc.
Click me to see the sample solution'''

import pandas as pd
import numpy as np
pi = pd.Series(np.random.randn(36), 
               pd.period_range('1/1/2029', 
                               '12/31/2031', freq='M'))
print("PeriodIndex which represents all the calendar month periods in 2029 and 2030:")
print(pi)
print("\nValues for all periods in 2030:")
print(pi['2030'])

'''30. Write a Pandas program to generate holidays between two dates using the US federal holiday calendar. 
Click me to see the sample solution'''

import pandas as pd
from pandas.tseries.holiday import *
sdt = datetime(2021, 1, 1)
edt = datetime(2030, 12, 31)
print("Holidays between 2021-01-01 and 2030-12-31 using the US federal holiday calendar.")
cal = USFederalHolidayCalendar()
for dt in cal.holidays(start=sdt, end=edt): 
    print (dt)

'''31. Write a Pandas program to create a monthly time period and display the list of names in the current local scope. 
Click me to see the sample solution'''

import pandas as pd
mtp = pd.Period('2021-11','M')
print("Monthly time perid: ",mtp)
print("\nList of names in the current local scope:")
print(dir(mtp)) 

'''32. Write a Pandas program to create a yearly time period from a specified year and display the properties of this period. 
Click me to see the sample solution'''

import pandas as pd
ytp = pd.Period('2020','A-DEC')
print("Yearly time perid:",ytp)
print("\nAll the properties of the said period:")
print(dir(ytp))

