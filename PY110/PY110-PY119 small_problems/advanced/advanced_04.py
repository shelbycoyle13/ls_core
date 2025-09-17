# Write a function that takes two sorted lists as arguments and returns a new list that contains all the elements from both input lists in ascending sorted order. You may assume that the lists contain either all integer values or all string values.

# You may not provide any solution that requires you to sort the result list. You must build the result list one element at a time in the proper order.

# Your solution should not mutate the input lists.

# All of these examples should print True
# print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
# print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
# print(merge([], [1, 4, 5]) == [1, 4, 5])
# print(merge([1, 4, 5], []) == [1, 4, 5])

# names1 = ['Alice', 'Kim', 'Pete', 'Sue']
# names2 = ['Bonnie', 'Rachel', 'Tyler']
# names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
#                   'Rachel', 'Sue', 'Tyler']
# print(merge(names1, names2) == names_expected)

"""
P
input = two lists
output = one combined list, sorted in ascending order
explicit = we're not allowed to sort the final list, we have to build the final list one element at a time
implicit = list argument could be empty. lists could be different lengths

E
# print(merge([5, 2, 8], [9, 0]) == [0, 2, 5, 8, 9])

D
lists

A
-first, since we're not allowed to mutate the original lists, make copies of them
-initialize an empty final list
-use a while loop to keep track if both lists are truthy or that they still have elements (if one of the lists becomes empty, the while loop breaks)
    -if the first element of the copy of list1 is less than or equal to the copy of list2
        -pop this element and append it to the empty final list
    -else
        -pop the first element of the copy of list2 and append to the final list
-at some point, because the lists may be of different lengths, the loop will break, and one of the lists may still have elements in them, we want to return the final list plus list copy1 and list copy 2. concatenating these lists creates one new list

C
"""
def merge(list1, list2):
    copy1 = list1[:]
    copy2 = list2[:]
    result = []

    while copy1 and copy2:
        if copy1[0] <= copy2[0]:
            result.append(copy1.pop(0))
        else:
            result.append(copy2.pop(0))

    return result + copy1 + copy2