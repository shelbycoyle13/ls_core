# Write a function that takes one argument, a positive integer, and returns the sum of its digits.

# print(sum_digits(23) == 5)              # True
# print(sum_digits(496) == 19)            # True
# print(sum_digits(123456789) == 45)      # True

"""
P
input = an integer
output = an integer (sum of its digits)
explicit = integer is always positive
implicit = 

E
# print(sum_digits(12345) == 15)              # True

D
looping?

A
-let's turn the number into a string so we can iterate through it
-for every string as digit in the entire string
    - add the digit (turned back into an integer) to the final list
-we want to sum the digits in the final list
-return the sum

C
"""

def sum_digits(num):
    digits = [int(digit) for digit in str(num)]
    return sum(digits)

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True
print(sum_digits(12345) == 15)              # True