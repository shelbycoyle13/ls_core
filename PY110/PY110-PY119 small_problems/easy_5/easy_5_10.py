# Given a sequence of integers, filter out instances where the same value occurs successively, retaining only the initial occurrence. Return the refined sequence.

# original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
# expected = [1, 2, 6, 5, 3, 4]
# print(unique_sequence(original) == expected)      # True

"""
P
input = a list of integers
output = a list of unique integers
explicit = we're only keeping unique integers
implicit = the integers do have to maintain the same order as what is returned

E
# original = [5, 5, 6, 6, 7, 8, 9, 9]
# expected = [5, 6, 7, 8, 9]
# print(unique_sequence(original) == expected)      # True

D
lists
sets

A
-coerce the list into a set
-coerce the set back into a list
-return the final list

C
"""

def unique_sequence(lst):
    final_lst = []
    for num in lst:
        if num not in final_lst:
            final_lst.append(num)
    return final_lst

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True

original = [5, 5, 6, 6, 7, 8, 9, 9]
expected = [5, 6, 7, 8, 9]
print(unique_sequence(original) == expected)      # True