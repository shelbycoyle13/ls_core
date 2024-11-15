# After Midnight (Part 1)
# The time of day can be represented as the number of minutes before or after midnight. If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

# Write a function that takes a time using this minute-based format and returns the time of day in 24-hour format (hh:mm). Your function should work with any integer input.

# You may not use Python's datetime module.

# print(time_of_day(0) == "00:00")        # True
# print(time_of_day(-3) == "23:57")       # True
# print(time_of_day(35) == "00:35")       # True
# print(time_of_day(-1437) == "00:03")    # True
# print(time_of_day(3000) == "02:00")     # True
# print(time_of_day(800) == "13:20")      # True
# print(time_of_day(-4231) == "01:29")    # True

# P
# input = an integer, could be negative
# output = a string
# explicit = our argument represents minutes. if the integer is negative, we subtract from 24:00. if it's positive, we add to 00:00.
# implicit = even an integer of 0, results in 00:00. We're not allowed to use the datetime module.

# E
# print(time_of_day(-60) == "23:00")       # True

# D
# if statements

# A
# First we sort by positive or negative numbers
    # If a number if positive, let's divide by 60 to get the hours
        # if hours exceed 24, subtract 24 until you can't anymore
    # Then, using the numbers after the decimal, multiply by 60 again to get the remaining number of minutes
    # Add this to 00:00

    # If a number is negative, let's divide by 60 to get the hours
    # Then, using the numbers after the decimal, multiply by 60 again to get the remaining number of minutes
    # Subtract these from 24:00
# Return these numbers as a string

# C
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = MINUTES_PER_HOUR * HOURS_PER_DAY   #1440

def format_time(hours, minutes):
    return f"{hours:02d}:{minutes:02d}"

def time_of_day(delta_minutes):
    while delta_minutes < 0:
        delta_minutes += MINUTES_PER_DAY
    
    delta_minutes = delta_minutes % MINUTES_PER_DAY
    hours = delta_minutes // MINUTES_PER_HOUR
    minutes = delta_minutes % MINUTES_PER_HOUR

    return format_time(hours, minutes)

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True
print(time_of_day(-60) == "23:00")      # True