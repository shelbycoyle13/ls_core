# Convert a String to a Signed Number
# In the previous exercise, you developed a function that converts simple numeric strings to integers. In this exercise, you're going to extend that function to work with signed numbers.

# Write a function that takes a string of digits and returns the appropriate number as an integer. The string may have a leading + or - sign; if the first character is a +, your function should return a positive number; if it is a -, your function should return a negative number. If there is no sign, return a positive number.

# You may assume the string will always contain a valid number.

# You may not use any of the standard conversion functions available in Python, such as int. You may, however, use the string_to_integer function from the previous exercise.

# P 
# input = string
# output = integer, with a leading symbol
# explicit = we are allowed to build off the previous function we have. if the string does not include a symbol, return a positive number. 
# implicit = 

# E
# Examples / test cases are above

# D
# Dictionary, for loop

# A
# - Without being able to use the int() constructor function, how else can we convert a string to an integer? We can use a dictionary. Set the keys as strings (each number representing a single-digit integer) and the values are the actual integer. This time we will also include symbols.
# - We set an initial value of 0.
# - Now we can use our for loop to iterate through each character of the string.
# - Let's include an if statement to deal with the symbols first.
# - Then for each character that is a number, we are going to reassign the "value" to (10 * value) + the value of the key in the dictionary. For the value, we can use the matching "character"
# - Multiplying by 10 will continue to increase the integer as well as move the integer "to the left" while adding the new integer in the ones place
# - When the loop is finished, we can return the final "value"

# C
def string_to_signed_integer(string):
    numbers_dict = {
        '0' : 0,
        '1' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9,
        '-' : 0,
        '+' : 0
    }

    value = 0

    for char in string:
        value = (10 * value) + numbers_dict[char]

    if string.startswith("+"):
        signed_value = 0
        signed_value += +value

        return signed_value 

    if string.startswith("-"):
        signed_value = 0
        signed_value += -value

        return signed_value

    else:
        return value

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True
