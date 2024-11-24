# Write a function that rotates a list by moving the first element to the end of the list. Do not modify the original list; return a new list instead.

# If the input is an empty list, return an empty list.
# If the input is not a list, return None.
# Review the test cases below, then implement the solution accordingly.

# # All of these examples should print True

# print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
# print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
# print(rotate_list(['a']) == ['a'])
# print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
# print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
# print(rotate_list([]) == [])

# # return `None` if the argument is not a list
# print(rotate_list(None) == None)
# print(rotate_list(1) == None)

# # the input list is not mutated
# lst = [1, 2, 3, 4]
# print(rotate_list(lst) == [2, 3, 4, 1])
# print(lst == [1, 2, 3, 4])

"""
P
input = expecting a list, but we can accept other object types
output = if a list, return a list. if not a list, return None
explicit = we need to move the first element of the list to the last index. we are returning a new list.
implicit = 

E
# print(rotate_list([1, 2, 3, 4, 5]) == [2, 3, 4, 5, 1])

D
lists

A
-final list initialized as empty list
-if argument given is not a list
    return None
-if argument given is an empty list
    return an empty list
-else
    iterate through the current list
        if index is zero
            continue
        else
            append to the new final list
-iterate through the current list
    if index is zero
        append to new final list
    else
        continue
return final list

C
"""
def rotate_list(lst):
    final_list = []

    if not isinstance(lst, list):
        return None
    if lst == []:
        return []
    else:
        for i, element in enumerate(lst):
            if i == 0:
                continue
            else:
                final_list.append(element)
        for i, element in enumerate(lst):
            if i == 0:
                final_list.append(element)
            else:
                continue
    return final_list

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])

print(rotate_list([1, 2, 3, 4, 5]) == [2, 3, 4, 5, 1])