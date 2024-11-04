# Find the Duplicate
# Given an unordered list and the information that exactly one value in the list occurs twice (every other value occurs exactly once), determine which value occurs twice. Write a function that finds and returns the duplicate value.

# You may assume that the input list will always have exactly one duplicate value.

# P
# input = list
# output = 1 duplicate value
# explicit = only one value in the list occurs twice. every other value occurs only once. each list will always have one duplicate value.
# Implicit = each list will have at least two values

# E
# print(find_dup([1, 5, 3, 7, 9, 9]) == 9) # True

# D
# lists, possibly for loop

# A
# we can loop through the list
# set a count to 0
# if count rises to 2, return that number

# print(find_dup([1, 5, 3, 1]) == 1) # True
# print(find_dup([
#                   18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
#                   38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
#                   14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
#                   78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
#                   89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
#                   41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
#                   55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
#                   85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
#                   40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
#                    7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
#               ]) == 73)       # True

# C

def find_dup(lst):
    for num in lst:
        if lst.count(num) == 2:
            return num
            
print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True
print(find_dup([1, 5, 3, 7, 9, 9]) == 9) # True