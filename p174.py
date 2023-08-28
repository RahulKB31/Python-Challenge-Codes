#900

'''
Convert date string to timestamp in Python
'''

# convert date string to timestamp using timetuple()

import time
import datetime

string = "20/01/2020"
print(time.mktime(datetime.datetime.strptime(string,"%d/%m/%y").timetuple()))

#################################################################################################################

#901

import time
import datetime

string = "20/01/2020"

element  = datetime.datetime.strptime(string,"%d/%m/%y")

tuple = element.timetuple()
timestamp = time.mktime(tuple)

print(timestamp)

##################################################################################################################

#902

'''
Convert date string to time stamp using timestamp()
'''

import time
import datetime

string = "20/01/2020"

element = datetime.datetime.strptime(string,"%d/%m/%Y")

timestamp = datetime.datetime.timestamp(element)
print(timestamp)

#################################################################################################################

































































































