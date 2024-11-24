# Transform two lists into frozen sets and find their common elements.

# list1 = [2, 4, 6, 8]
# list2 = [1, 3, 5, 7, 8]
# expected_result = frozenset({8})
# print(intersection(list1, list2) == expected_result) # True

"""
P
input = two lists
output = one frozen set
explicit = we are looking for the common element(s) between the lists / frozen sets
implicit = perhaps there may not be any common elements

E
# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 6, 7, 8, 9]
# expected_result = frozenset({5})
# print(intersection(list1, list2) == expected_result) # True

D
lists
frozen sets

A
-transform the two lists into frozen sets
-use the intersection method to get the common elements
-return the frozen set

C
"""

def intersection(lst1, lst2):
    return frozenset(lst1) & frozenset(lst2)

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True

# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 6, 7, 8, 9]
# expected_result = frozenset({5})
# print(intersection(list1, list2) == expected_result) # True