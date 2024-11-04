# Cute Angles
# Write a function that takes a floating point number representing an angle between 0 and 360 degrees and returns a string representing that angle in degrees, minutes, and seconds. You should use a degree symbol (°) to represent degrees, a single quote (') to represent minutes, and a double quote (") to represent seconds. There are 60 minutes in a degree, and 60 seconds in a minute.

# Note: You can use the following constant to represent the degree symbol:

# DEGREE = "\u00B0"

# # All of these examples should print True
# print(dms(30) == "30°00'00\"")
# print(dms(76.73) == "76°43'48\"")
# print(dms(254.6) == "254°35'59\"")
# print(dms(93.034773) == "93°02'05\"")
# print(dms(0) == "0°00'00\"")
# print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

# P
# input = float
# output = string, with symbols
# explicit = the float we have as an argument represents an angle between 0 - 360. The degree symbol represents degrees, single quote represents minutes, double quote represents seconds. There are 60 minutes in a degree. It looks like the minutes are calculated by taking the numbers after the decimal place and multiplying by 60. Then, we take that result, take the numbers after the decimal place, and multiply by 60 to get the seconds.
# Implicit = If we receive an integer as an argument, we still transform this into minutes and seconds. Looks like we are not accepting negative numbers here. The rules don't say that we aren't allowed to use the str() constructor function this time.

# E
# print(dms(100) == "100°00'00\"")

# D
# strings, while loop, if else blocks

# A
# Set an empty string. ""
# We could start with a if statement checks if the number is greater than or equal to 0.
# If the integer is a whole number with no decimal places, we could return the number into a string.
    # We can take the integer and use str() to add to the empty string.
    # We must then add the constant variable to access the degree symbol. Add to empty string.
    # We then add 00' and 00\" to the empty string
# If the integer is a float, we'll need to do additional calculations to figure out the minutes and seconds.
    # To calculate minutes, we need to take the decimal place and the numbers after and multiply by 60.
    # Take the whole number, coerce to a string, add the ' to the final string
    # To calculate the seconds, take the decimal place and the numbers after, multiply by 60.
    # Take the whole number, coerce to a string, add the \" to the final string
# Return the final string

import math

DEGREE = "\u00B0"
QUOTE = "'"
DOUBLE_QUOTE = "\""

def dms(number):

    final_string = ""

    if number >= 0:
        if number % 2 == 0:
            number_as_string = str(number)
            final_string += number_as_string + DEGREE + "00"+ QUOTE + "00" + DOUBLE_QUOTE
            return final_string
        else:
            rounded_number = str(math.floor(number / 1))
            after_decimal_once = number % 1
            minutes = after_decimal_once * 60
            after_decimal_twice = minutes % 1
            seconds = after_decimal_twice * 60
            minutes_string = str(int(minutes))
            if len(minutes_string) == 1:
                minutes_string = str(0) + minutes_string
            seconds_string = str(int(seconds))
            if len(seconds_string) == 1:
                seconds_string = str(0) + seconds_string
            final_string += rounded_number + DEGREE + minutes_string + QUOTE + seconds_string + DOUBLE_QUOTE
            return final_string
            

print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")