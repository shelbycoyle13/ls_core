# Convert a String to a Number

# Write a function that takes a string of digits and returns the appropriate number as an integer. You may not use any of the standard conversion functions available in Python, such as int. Your function should calculate the result by using the characters in the string.

# For now, do not worry about leading + or - signs, nor should you worry about invalid characters; assume all characters are numeric.

# print(string_to_integer("4321") == 4321)  # True
# print(string_to_integer("570") == 570)    # True

# To compute an integer value from a string of digits, you should know that the rightmost digit is the "ones" digit; that is, it contributes its value to the overall result. If there's another digit to the left of that digit, that digit is the "tens" digit; it contributes its value times 10 to the overall result.

# To convert a string like "5372" to an integer, you need to understand how our decimal numbers work. In this case, 2 is in the "ones" position, 7 is in the tens position, 3 in the hundreds position, and 5 in the thousands position:

# digits	5	3	7	2
# ones				2
# tens			70	
# hundreds		300		
# thousands	5000			
# Thus, we can calculate the numeric value of "5372" as 5000 + 300 + 70 + 2, or 5372.

# P 
# input = a string (that looks like an integer)
# output = an integer
# explicit = we can't use int().
# implicit = we're allowed to use the characters of a string to figure out that the right-hand most digit is the ones place, then to the left is the tens place, then hundreds, then thousands.

# E
# Examples / test cases are above

# D
# For loop, dictionary

# A
# - Without being able to use the int() constructor function, how else can we convert a string to an integer? We can use a dictionary. Set the keys as strings (each number representing a single-digit integer) and the values are the actual integer.
# - We set an initial value of 0.
# - Now we can use our for loop to iterate through each character of the string.
# - For each character, we are going to reassign the "value" to (10 * value) + the value of the key in the dictionary. For the value, we can use the matching "character"
# - Multiplying by 10 will continue to increase the integer as well as move the integer "to the left" while adding the new integer in the ones place
# - When the loop is finished, we can return the final "value"

# C
def string_to_integer(string):
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
        '9' : 9
    }

    value = 0

    for char in string:
        value = (10 * value) + numbers_dict[char]
    return value

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True