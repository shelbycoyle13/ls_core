# Given two lists, convert them to sets and return a new set which is the union of both sets.

# list1 = [3, 5, 7, 9]
# list2 = [5, 7, 11, 13]
# print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True

"""
P
input = two lists
output = one set
explicit = convert both lists to sets and return one set
implicit = 

E
# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 6, 7, 8, 9]
# print(merge_sets(list1, list2) == {1, 2, 3, 4, 5, 6, 7, 8, 9})
# Prints True

D
lists, sets

A
-convert each list to a set using set()
-use .union or | to combine the sets into one new set
-return the new set

C
"""

def merge_sets(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    new_set = set1.union(set2)
    return new_set

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13}) # Prints True
# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 6, 7, 8, 9]
# print(merge_sets(list1, list2) == {1, 2, 3, 4, 5, 6, 7, 8, 9}) # Prints True