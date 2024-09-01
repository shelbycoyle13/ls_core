# Write a function that takes a year as input and returns the century. The return value should be a string that begins with the century number, and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.

# New centuries begin in years that end with 01. So, the years 1901 - 2000 comprise the 20th century.

import math

def century(year):
    century_short = math.ceil(year / 100)
    century_short_string = str(century_short)

    if century_short_string.endswith("11"):
        return century_short_string + "th"
    elif century_short_string.endswith("12"):
        return century_short_string + "th"
    elif century_short_string.endswith("13"):
        return century_short_string + "th"
    elif century_short_string.endswith("1"):
        return century_short_string + "st"
    elif century_short_string.endswith("2"):
        return century_short_string + "nd"
    elif century_short_string.endswith("3"):
        return century_short_string + "rd"
    else:
        return century_short_string + "th"

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True