# List Average
# Write a function that takes one argument, a list of integers, and returns the average of all the integers in the list, rounded down to the integer component of the average. The list will never be empty, and the numbers will always be positive integers.

# print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
# print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
# print(average([7]) == 7)                          # True

# P
# input = list
# output = integer
# explicit = the average will be rounded down to just the integer. the list will never be empty. the numbers will always be positive.
# implicit = 

# E
# print(average([1, 2, 3, 4, 5, 6]) == 3)        # True


# D
# lists, for loops

# A
# take the sum of the integers in the list
# divide by the length of the list
# the average should be rounded down to just the integer

# C

def average(lst):
    add_all_elements = sum(lst)
    average = add_all_elements // len(lst)
    return average

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True
print(average([1, 2, 3, 4, 5, 6]) == 3)        # True
