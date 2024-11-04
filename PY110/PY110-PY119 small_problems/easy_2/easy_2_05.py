# Combine Two Lists
# Write a function that combines two lists passed as arguments and returns a new list that contains all elements from both list arguments, with each element taken in alternation.

# You may assume that both input lists are non-empty, and that they have the same number of elements.

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# expected = [1, "a", 2, "b", 3, "c"]
# print(interleave(list1, list2) == expected)      # True

# P
# input = two lists
# output = one new list, with elements of the previous two alternating
# explicit = both lists will have the same amount of elements
# Implicit = 

# E
# list1 = ["apples", "oranges", "lemons"]
# list2 = [5, 6, 7]
# expected = ["apples", 5, "oranges", 6, "lemons", 7]

# D
# lists

# A
# define a function and include the zip function within it
# the result of zip are tuples. zip is also lazy, we must wrap it in a list
# we could iterate over this list, and unpack the tuples
# add the unpacked elements to a new empty list
# return the final new list

# C

def interleave(lista, listb):
    zipped_list = list(zip(lista, listb))
    final_list = []

    for tup in zipped_list:
        n, l = tup
        final_list.append(n)
        final_list.append(l)
    return final_list

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)

# list1 = ["apples", "oranges", "lemons"]
# list2 = [5, 6, 7]
# expected = ["apples", 5, "oranges", 6, "lemons", 7]
# print(interleave(list1, list2) == expected)