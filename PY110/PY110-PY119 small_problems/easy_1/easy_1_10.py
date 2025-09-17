# Convert a Number to a String

# In the previous two exercises, you developed functions that convert simple numeric strings to signed integers. In this exercise and the next, you're going to reverse those functions.

# Write a function that converts a non-negative integer value (e.g., 0, 1, 2, 3, and so on) to the string representation of that integer.

# You may not use any of the standard conversion functions available in Python, such as str. Your function should do this the old-fashioned way and construct the string by analyzing and manipulating the number.

# print(integer_to_string(4321) == "4321")              # True
# print(integer_to_string(0) == "0")                    # True
# print(integer_to_string(5000) == "5000")              # True
# print(integer_to_string(1234567890) == "1234567890")  # True

# P 
# input = integer
# output = string
# explicit =  we can't use the str() constructor function
# implicit = 

# E
# Examples / test cases are above

# D
# For loop, dictionary?

# A
# - We could create a dictionary with the integers as the keys and the values as the strings
# - Create an empty string
# - 
# - For every integer, add that value to an empty string
# - Return the final string

# C
def integer_to_string(integer):

    integer_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    final_string = ""
    
    while integer > 0: #4321
        integer, remainder = divmod(integer, 10) #integer, remainder = divmod(4321, 10) = (432, 1)
        final_string = integer_list[remainder] + final_string # '1' + final_string
    return final_string or '0'

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True