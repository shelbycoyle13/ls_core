# Take the number 735291 and rotate it by one digit to the left, getting 352917. Next, keep the first digit fixed in place and rotate the remaining digits to get 329175. Keep the first two digits fixed in place and rotate again to get 321759. Keep the first three digits fixed in place and rotate again to get 321597. Finally, keep the first four digits fixed in place and rotate the final two digits to get 321579. The resulting number is called the maximum rotation of the original number.

# Write a function that takes an integer as an argument and returns the maximum rotation of that integer. You can (and probably should) use the rotate_rightmost_digits function from the previous exercise.

# print(max_rotation(735291) == 321579)          # True
# print(max_rotation(3) == 3)                    # True
# print(max_rotation(35) == 53)                  # True
# print(max_rotation(8703529146) == 7321609845)  # True

# # Note that the final sequence here is `015`. The leading
# # zero gets dropped, though, since we're working with
# # an integer.
# print(max_rotation(105) == 15)                 # True

"""
P
input = integer
output = integer (after maximum rotation)
explicit = the number of rotations the integer will go through is the length of the integer - 1. the first rotation starts with the left-most integer and moves it to the end. the second rotation moves the second integer from the left, etc.
implicit = it's possible that a 0 may end up at the left-most place in the integer. this would get dropped.

E
# print(max_rotation(123) == 213)          # True

D
strings

A
-the number of digits = the length of the number. first, coerce the integer to a string
-we want to utilize count from the last function we made. count in the last function was the same as the digit place. in this current problem, we are also iterating through the index places. although we are going from 0, 1, 2...etc to the end of the string, you can still look at this as -length of string, ...-3, -2. Our maximum rotation stops at the -2 index for numbers with a length > 1. so our range will move in a negative step.
-> so for every count in the range starting at the most negative indexed number, counting down to the stop number of 1
-our new number will equal the return value of calling the previous function, passing in the number argument and our count (which is what is currently being iterated through)
-we then return the final number

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

def max_rotation(number):
    number_digits = len(str(number))
    for count in range(number_digits, 1, -1): #Don't forget you can have a range with a negative step
        number = rotate_rightmost_digits(number, count)

    return number