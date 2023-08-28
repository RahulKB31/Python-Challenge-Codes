#903

'''
How to convert timestamp string to datetime object in python
'''

#Using strptime()

from datetime import datetime

timestamp_string = "2023-07-21 15:30:45"
format_string = "%Y-%m-%d %H:%M:%S"
datetime_object = datetime.strptime(timestamp_string,format_string)
print(datetime_object)

################################################################################################################

#904

'''
Using datetime.strptime()
'''

from datetime import datetime

timestamp = 154347892002
dt_obj = datetime.fromtimestamp(116048394300)

print("date time: ", dt_obj)
print('type of dt: ', type(dt_obj))

##############################################################################################################

#905

'''
Using dateutil.parseer.parse()
'''

from dateutil.parser import parser

timestamp_string = "2023-07-21 15:30:45"

datetime_object = parse(timestamp_string)
print(datetime_object)

###############################################################################################################

#906

'''
Using Datetime.from timestamp()
'''

import datetime

timestamp = 1690433696

dt_object = datetime.datetime.fromtimestamp(timestamp)
print(dt_object)

#################################################################################################################




































































































