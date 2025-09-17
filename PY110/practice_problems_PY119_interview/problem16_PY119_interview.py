# Problem 16
# Create a function that returns the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. You may assume that the input string contains only alphanumeric characters.

# print(distinct_multiples('xyz') == 0)               # (none)
# print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
# print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
# print(distinct_multiples('unununium') == 2)         # u, n
# print(distinct_multiples('multiplicity') == 3)      # l, t, i
# print(distinct_multiples('7657') == 1)              # 7
# print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
# print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5

# The above tests should each print True.

"""
P
input = a string
output = an integer
explicit = we are returning the amount of characters that occur more than once in the string
implicit = 

E

D
strings

A
-initialize count of 0
-iterate through the string, for char in string
    -if string.count(char) > 1
        -count += 1

-return count

C
"""
def distinct_multiples(string):
    count = 0

    for char in set(string.casefold()):
        if string.casefold().count(char) > 1:
            count += 1
    
    return count

print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5

#Second approach
def distinct_multiples(string):
    count = 0

    for char in set(string.casefold()):
        if string.casefold().count(char) > 1:
            count += 1
    
    return count