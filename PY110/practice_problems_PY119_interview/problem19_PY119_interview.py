# Create a function that takes a list of integers as an argument and returns the integer that appears an odd number of times. There will always be exactly one such integer in the input list.

# The above tests should each print True.

# print(odd_fellow([4]) == 4)
# print(odd_fellow([7, 99, 7, 51, 99]) == 51)
# print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
# print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
# print(odd_fellow([0, 0, 0]) == 0)

"""
P
input = a list (of integers)
output = an integer
explicit = we want to return the integer that appears an odd number of times. There will only be one of these integers per list.
implicit = we are including negative numbers and 0 in our lists and returned numbers

E

D
lists

A
-iterate through the list, for num in char
    -if list.count(num) % 2 == 1
        -return num

C
"""

def odd_fellow(lst):
    for num in lst:
        if lst.count(num) % 2 == 1:
            return num
        
print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)