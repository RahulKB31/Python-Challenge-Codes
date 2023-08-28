#878

'''
Python program to get current time
'''

from datetime import *
import pytz

tz_INDIA = pytz.timezone('Asia/Kolkata')
datatime_INDIA = datetime.now(tz_INDIA)
print("India time:", datatime_INDIA.strftime("%H:%M:%S"))

#################################################################################################################

#879

from datetime import datetime

now_method = datetime.now()

currentTime = now_method.strftime("%H:%M:%S")
print("Current Time =", currentTime)

################################################################################################################

#880

from datetime import datetime

time = datetime.now().time()
print("Current time =", time)

##################################################################################################################

#881

import time

Time = time.localtime()

currentTime = time.strftime("%H:%M:%S",Time)
print(currentTime)

##################################################################################################################































