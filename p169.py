#882

'''
How to get Current date and time using python
'''

# current date-time using Date Time

import datetime

current_time= datetime.datetime.now()
print("Time now at greenwich meridian is:", current_time)

############################################################################################################

#883

'''
Attributes of DateTime using DateTime
'''

import datetime

current_time = datetime.datetime.now()

print("The attributes of now() are: ")

print("Year:", current_time.year)
print("Month:", current_time.month)
print("Day:", current_time.day)
print("Hour:", current_time.hour)
print("Minute:", current_time.minute)
print("Second:", current_time.second)
print("Microsecond:", current_time.microsecond)

###################################################################################################################

#884

'''
Get a particular timezone using pytz and datetime
'''

import datetime

import pytz

current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

print("The current time in India is: ", current_time)

##################################################################################################################

#885

'''
Get current Time in UTC using datetime
'''

from datetime import datetime

print("UTC Time:", datetime.utcnow())

#############################################################################################################

#886

'''
Get current time in ISO format using datetime
'''

from datetime import datetime as dt

x = dt.now().isoformat()
print("Current ISO:",x)

#################################################################################################################

#887

'''
get current time using the time module
'''

import time

curr_time = time.struct_time("%H:%M:%S", time.localtime())
print("Current time is:", curr_time)

#################################################################################################################

#888

'''
get current time in millisecond using time
'''

import time
millisec = int(round(time.time() * 1000))
print("Time in millisecond:", millisec)

#################################################################################################################

#889

'''
get current time in nanoseconds using time
'''

import time
current_time = time.struct_time("%H:%M:%S", time.localtime())
print("Current time is;", curr_time)
nano_seconds = time.time_ns()
print("Current time in nano seconds is:", nano_seconds)

#################################################################################################################

#890

'''
get current GMT using time
'''

import time
gmt_time = time.gmtime(time.time())
print("Current GMT Time:\n",gmt_time)

#################################################################################################################

#891

'''
get current time in epoch using time
'''

import time
print("Epoch Time is:", int(time.time()))

#################################################################################################################










































