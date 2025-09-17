# 45. Count Digit Occurences
# Your goal is to write the group_and_count function, which should receive a list as a unique parameter and return a dictionary. Empty or None input must return None instead of a dictionary. This dictionary returned must contain as keys the unique values of the list, and as values the counting of each value.

#print(group_and_count([1,1,2,2,2,3]) == {1: 2, 2: 3, 3: 1})
#print(group_and_count([]) == None)
#print(group_and_count(None) == None)
#print(group_and_count([1, 7, 5, -1]) == {1: 1, 7: 1, 5: 1, -1: 1})

"""
P
input = a list, or None
output = a dictionary, or None
explicit = we take a list as an input. if the list is truthy, we return a dictionary. the keys are the unique elements of the list, the values are the number of occurrences of that element
implicit =  looks like the order of the keys matches the order in the list

E

D
lists
dictionary

A
if list is None:
    return None
initialize dict
iterate through the set of the list, for num in list
    dict[num] == list.count(num)

return dict

C
"""

def group_and_count(lst):
    if lst is None or lst == []:
        return None
    
    dict_count = {}

    for num in set(lst):
        dict_count[num] = lst.count(num)

    return dict_count


print(group_and_count([1,1,2,2,2,3]) == {1: 2, 2: 3, 3: 1})
print(group_and_count([]) == None)
print(group_and_count(None) == None)
print(group_and_count([1, 7, 5, -1]) == {1: 1, 7: 1, 5: 1, -1: 1})