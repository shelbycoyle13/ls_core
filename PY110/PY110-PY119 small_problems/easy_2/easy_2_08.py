# List of Digits
# Write a function that takes one argument, a positive integer, and returns a list of the digits in the number.

# print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
# print(digit_list(7) == [7])                       # True
# print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
# print(digit_list(444) == [4, 4, 4])               # True

# P
# input = an integer
# output = a list
# explicit = we are returning a list of the digits in the integer; the first element in the list is the first number we see in the integer, starting from the left
# implicit = looks like we cannot have an empty argument

# E
# print(digit_list(4567) == [4, 5, 6, 7])       # True 

# D
# strings and a for loop

# A
# Set an empty final list
# change the integer to a string
# iterate through the string
# for every char, change back to an integer
# add the integer to the final list
# return the final list

# C

def digit_list(int1):
    final_list = []

    int_as_string = str(int1)

    for char in int_as_string:
        char_to_int = int(char)
        final_list.append(char_to_int)
    return final_list
    
print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True
print(digit_list(4567) == [4, 5, 6, 7])       # True 