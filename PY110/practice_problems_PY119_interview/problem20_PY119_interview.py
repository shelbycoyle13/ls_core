# Problem 20
# Create a function that takes a list of numbers, all of which are the same except one. Find and return the number in the list that differs from all the rest.

# The list will always contain at least 3 numbers, and there will always be exactly one number that is different.

# The below tests should each print True.

# print(what_is_different([0, 1, 0]) == 1)
# print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
# print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
# print(what_is_different([3, 4, 4, 4]) == 3)
# print(what_is_different([4, 4, 4, 3]) == 3)

"""
P
input = a list (of numbers)
output = a number 
explicit = we want to return the number in the list that is different from all of the rest
implicit = the number we want returned could be an integer or a float

E
# print(what_is_different([1, 2, 1, 1]) == 2)

D
list

A
-iterate through the list, for num in list
    -if list.count(num) == 1
        -return num

C
"""
def what_is_different(lst):
    for num in lst:
        if lst.count(num) == 1:
            return num

print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)
print(what_is_different([1, 2, 1, 1]) == 2) 

#Second answer, longer but incorporates a list comp:

# def what_is_different(lst):

#     final_list = [num for num in lst if lst.count(num) == 1]

#     return final_list[0]