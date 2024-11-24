# Write a function that takes an integer argument and returns a list containing all integers between 1 and the argument (inclusive), in ascending order.

# You may assume that the argument will always be a positive integer.

# print(sequence(5) == [1, 2, 3, 4, 5])   # True
# print(sequence(3) == [1, 2, 3])         # True
# print(sequence(1) == [1])               # True

"""
P

input = integer
output = list
explicit = argument is inclusive in the list. We want to count upwards towards the argument starting at 1
implicit = even if there is only one number in the list, we want to still return the integer in a list

E
# print(sequence(4) == [1, 2, 3, 4]) 

D
range

A
- let's try a list comprehension this time. for each number in the range starting at 1 up to and including the argument, return the number

C
"""
def sequence(high_number):
    new_list = [num for num in range(1, high_number + 1)]
    return new_list

print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True
print(sequence(4) == [1, 2, 3, 4])      # True