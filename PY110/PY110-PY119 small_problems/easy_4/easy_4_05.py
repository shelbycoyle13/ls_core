# From two list arguments, determine the elements that are unique to the first list. The return value should be a set.

# list1 = [3, 6, 9, 12]
# list2 = [6, 12, 15, 18]
# print(unique_from_first(list1, list2) == {9, 3})

"""
P
input = two lists
output = one set
explicit = we want unique elements from the first list
implicit = 

E
# list1 = [1, 2, 3, 4]
# list2 = [4, 5, 6, 7]
# print(unique_from_first(list1, list2) == {1, 2, 3})

D
lists
sets

A
-turn both lists into sets
-use the difference between sets to return the unique elements of the first set

C
"""

def unique_from_first(lst1, lst2):
    return set(lst1) - set(lst2)

list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})

list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]
print(unique_from_first(list1, list2) == {1, 2, 3})