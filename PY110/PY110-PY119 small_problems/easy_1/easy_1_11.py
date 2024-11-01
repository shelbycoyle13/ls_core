# Convert a Signed Number to a String
# In the previous exercise, you developed a function that converts non-negative numbers to strings. In this exercise, you're going to extend that function by adding the ability to represent negative numbers as well.

# Write a function that takes an integer and converts it to a string representation.

# You may not use any of the standard conversion functions available in Python, such as str. You may, however, use integer_to_string from the previous exercise.

# print(signed_integer_to_string(4321) == "+4321")  # True
# print(signed_integer_to_string(-123) == "-123")   # True
# print(signed_integer_to_string(0) == "0")         # True

# P 
# input = integer
# output = string, with a symbol in front
# explicit =  we can't use the str() constructor function
# implicit = if the argument passed is 0, there is neither symbol used. no symbol passed automatically prepends a + to the returned string

# E
# Examples / test cases are above

# D
# strings

# A
# - Let's utilize the other function we created in the previous exercise. We have the final string returned.
# - We can use an if statement to check if the original integer starts with -. If so we can prepend the final string returned.
# - If the final string returns isn't 0, we could prepend a +.
# - Return the new final string

# C


        
def integer_to_string(integer):
        
    integer_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    final_string = ""
        
    while integer > 0:
        integer, remainder = divmod(integer, 10)
        final_string = integer_list[remainder] + final_string
    return final_string or '0'

def signed_integer_to_string(integer):
    if integer == 0:
        return "0"
    if integer < 0:
        signed_string = '-' + integer_to_string(-integer)
    if integer > 0:
        signed_string = '+' + integer_to_string(integer)
    
    return signed_string

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True