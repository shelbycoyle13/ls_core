# As seen in the previous exercise, the time of day can be represented as the number of minutes before or after midnight. If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

# Write two functions that each take a time of day in 24 hour format, and return the number of minutes before and after midnight, respectively. Both functions should return a value in the range 0 through 1439.

# You may not use Python's datetime module.

# Disregard Daylight Savings and Standard Time and other irregularities.

# print(after_midnight("00:00") == 0)     # True
# print(before_midnight("00:00") == 0)    # True
# print(after_midnight("12:34") == 754)   # True
# print(before_midnight("12:34") == 686)  # True
# print(after_midnight("24:00") == 0)     # True
# print(before_midnight("24:00") == 0)    # True

"""
P
input = string
output = integer
explicit = we are returning the number of minutes before and after midnight
implicit = both 00:00 and 24:00 return 0. all strings have 4 integers.

E
# print(after_midnight("07:15") == 435)   # True
# print(before_midnight("07:15") == 1005)   # True

D
possibly slicing?

A

AFTER_MIDNIGHT:
-let's take a slice of the string to get the hours -> string[0:2]
    - convert this to an integer
    - multiply by 60 = minutes
- to get the additional minutes, slice the string again -> string[3:]
    -convert to an integer
- add these two together to get the total number of minutes
- add total to 0 and return

BEFORE_MIDNIGHT:
- 1440 - AFTER

C
"""

def after_midnight(time):
    hours_to_minutes = int(time[0:2]) * 60
    adtl_minutes = int(time[3:])
    total_minutes = hours_to_minutes + adtl_minutes

    if total_minutes == 1440:
        total_minutes = 0
    return total_minutes

def before_midnight(minutes):
    
    if after_midnight(minutes) == 0:
        return 0
    return (1440 - after_midnight(minutes))


print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True

print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True

print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True

print(after_midnight("07:15") == 435)   # True
print(before_midnight("07:15") == 1005)   # True