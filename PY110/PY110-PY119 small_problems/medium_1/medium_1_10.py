# As we've seen in the last few exercises, the Fibonacci series is a computationally simple series, However, the results grow at an incredibly rapid rate. For example, the 100th Fibonacci number is 354,224,848,179,261,915,075 -- that's enormous, especially considering that it takes six iterations just to find the first 2-digit Fibonacci number.

# Write a function that calculates and returns the index of the first Fibonacci number that has the number of digits specified by the argument. The first Fibonacci number has an index of 1. You may assume that the argument is always an integer greater than or equal to 2.

# Since Python version 3.10.7, conversion of large integers to strings with more than 4300 digits raises an error. This means that the last test case will raise an error.

# To bypass this limitation, we can use set sys.set_int_max_str_digits from the sys module to a new upper limit. First, we import the sys module, then we call sys.set_int_max_str_digits with the maximum digits desired for string conversion.

# import sys

# sys.set_int_max_str_digits(50_000)

# # All of these examples should print True
# # The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
# print(find_fibonacci_index_by_length(2) == 7)
# print(find_fibonacci_index_by_length(3) == 12)
# print(find_fibonacci_index_by_length(10) == 45)
# print(find_fibonacci_index_by_length(16) == 74)
# print(find_fibonacci_index_by_length(100) == 476)
# print(find_fibonacci_index_by_length(1000) == 4782)

# # Next example might take a little while on older systems
# print(find_fibonacci_index_by_length(10000) == 47847)

"""
P
input = integer that represents the number / length of digits in an integer
output = integer that represents the "index" of the first integer of the argument's length
explicit = the argument will always be an integer that is equal or greater than 2
implicit = "indexes" don't start at 0, they start at 1

E

D

A
-we'll initialize a variable for the first and second integers in the sequence, both will have values of 1
-we'll initialize a variable for the "index" that we are at; it will have a value of 2
-we can't use len() on integers, so we have to coerce the integers to strings
-we'll use a similar formula that we used previously. we'll use tuple unpacking to reassign the first variable to the second, and the second to the second plus the first
-we'll use a while loop, as long as the length of the second (current) number we are on is less than the length we are looking for, continue the loop.
-we'll increment the "count" (or "index" we're on) by 1 on each iteration
-the while loop will end once the length of the current number string is greater than the length
-return the current count

C
"""

def find_fibonacci_index_by_length(length):
    first = 1
    second = 1
    count = 2

    while len(str(second)) < length:
        first, second = second, first + second
        count += 1
    
    return count

# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)