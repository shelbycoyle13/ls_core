# Combining Lists
# Write a function that takes two lists as arguments and returns a set that contains the union of the values from the two lists. You may assume that both arguments will always be lists.

# print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

# P
# input = two lists
# output = one set (union of the values)
# explicit = both arguments are always lists
# Implicit = we could use the .union() method

# E
# print(union([2, 4, 6], [3, 6, 9]) == {2, 3, 4, 6, 9}) # True

# D
# lists and sets

# A
# create a function with two list parameters
# use the set() constructor function on list 1 and list 2. assign these to new variables, respectively
# set 1 will call the .union() method on set 2. assign this to a new variable
# return new set variable

def union(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    set3 = set1.union(set2)
    return set3

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True
print(union([2, 4, 6], [3, 6, 9]) == {2, 3, 4, 6, 9}) # True