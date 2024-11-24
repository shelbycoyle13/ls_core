# Write a function that rotates the last count digits of a number. To perform the rotation, move the first of the digits that you want to rotate to the end and shift the remaining digits to the left.

# print(rotate_rightmost_digits(735291, 2) == 735219)  # True
# print(rotate_rightmost_digits(735291, 3) == 735912)  # True
# print(rotate_rightmost_digits(735291, 1) == 735291)  # True
# print(rotate_rightmost_digits(735291, 4) == 732915)  # True
# print(rotate_rightmost_digits(735291, 5) == 752913)  # True
# print(rotate_rightmost_digits(735291, 6) == 352917)  # True
# print(rotate_rightmost_digits(1200, 3) == 1002)      # True

"""
P
input = two integers, one is a "full" number, the other is the place of a digit starting from the right side
output = one new integer
explicit = the second number argument that is the place of the number we are trying to move to the end of the new number
implicit = 

E
# print(rotate_rightmost_digits(123456, 2) == 123465)  # True

D
strings

A
-take the number and coerce it into a string
-let's slice the first part of the string, first half equals the string[:-count]
-second slice equals string[-count:]
-with the second slice, we need to rotate the numbers, we can utilize the function we made in the previous exercise (using LS' answer)
-concatenate the two halves together
-coerce final string back into an integer
-return integer

C
"""
def rotate_list(string):
    return string[1:] + string[0]

def rotate_rightmost_digits(num, count):

    num_to_str = str(num)

    first_part = num_to_str[:-count]
    second_part = num_to_str[-count:]
    whole = first_part + rotate_list(second_part)
   
    str_to_num = int(whole)

    return str_to_num

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True
print(rotate_rightmost_digits(123456, 2) == 123465)  # True