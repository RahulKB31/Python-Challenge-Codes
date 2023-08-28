#894

'''
Python program to convert time from 12hour to 24hour format
'''

def convert24(str1):

    #checkiing if last two elements of time is AM and first two elements are 12
    if str[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]

    #remove the AM
    elif str1[-2:] == "AM":
        return str1[:-2]

    #checking if last two elements of time is PM and first two elements are 12
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]

    else:
        return str(int(str1[:2]) + 12) + str1[2:8]

print(convert24("08:05:45 PM"))

##################################################################################################################

#895

from datetime import datetime

def convert24(time):
    t = datetime.strptime(time, '%I:%M:%S %p')
    return t.strftime("%H:%M:%S")

print(convert24('11;21:30 PM'))
print(convert24('12:12:20 AM'))

#################################################################################################################

#896

'''
Using regular expression
'''

import re
def convert_to_24hour(time_str):
    hour, minute, second, am_pm = re.findall('\d+|\w+', time_str)
    hour = int(hour)
    if am_pm == "PM" and hour != 12:
        hour += 12
    elif am_pm == "AM" and hour == 12:
        hour = 0
    return f"{hour:02d}:{minute}:{second}"

print(convert_to_24hour('11:21:30 PM'))
print(convert_to_24hour('12:12:20 AM'))

#################################################################################################################

#897

'''
Using split()
'''

def convert_12_to_24(time_string):
    h,m,s = map(int, time_string[:-3].split(':'))
    suffix = time_string[-2:]
    offset = 0 if suffix == 'AM' else 12
    h = (h % 12) + offset
    return '{:02d}:{:02d}:{:02d}'.format(h,m,s)

input_time = '11:21:30 PM'
output_time = convert_12_to_24(input_time)
print("Input time: ", input_time)
print("Output Time:",output_time)

input_time = '12:12:20 AM'
output_time = convert_12_to_24(input_time)
print('Input time:', input_time)
print('Output time:', output_time)

##############################################################################################################





































































































