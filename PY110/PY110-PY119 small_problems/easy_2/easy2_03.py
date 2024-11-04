# Halvsies
# Write a function that takes a list as an argument and returns a list that contains two elements, both of which are lists. Put the first half of the original list elements in the first element of the return value and put the second half in the second element. If the original list contains an odd number of elements, place the middle element in the first half list.

# All of these examples should print True
# print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
# print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
# print(halvsies([5]) == [[5], []])
# print(halvsies([]) == [[], []])

# P
# input = one list
# output = 1 list with 2 sublists
# explicit = put the first half of the elements in the first sublist, second half in the second sublist. If there's an odd number of elements, put the middle element in the first sublist.
# Implicit = one element goes in the first sublist, empty sublist follows. empty list results in two empty sublists.

# E
# print(halvsies([1, 5, 2, 4, 3, 7]) == [[1, 5, 2], [4, 3, 7]])

# D
# lists

# A
# if the list is empty, create a new list with empty sublists
# if the list only has one element, create a sublist with the original list, and an empty sublist
# otherwise:
    # slice the list from the first index to the halfway point. set this to the first sublist
    # slice the list from the halfway point to the end of the list. set this to the second sublist
# return final list

def halvsies(lst):
    if len(lst) == 0:
        two_empty =  list(lst), list(lst)
        return list(two_empty)
    if len(lst) == 1:
        one_empty = list(lst), list()
        return list(one_empty)
    if len(lst) % 2 == 0:
        first_half = lst[:(len(lst) // 2)]
        second_half = lst[(len(lst) // 2):]
        whole = list(first_half), list(second_half)
        return list(whole)
    else:
        first_half = lst[:(len(lst) // 2) + 1]
        second_half = lst[(len(lst) // 2) + 1:]
        whole = list(first_half), list(second_half)
        return list(whole)
    
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])