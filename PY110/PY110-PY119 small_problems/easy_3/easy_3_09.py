# Write a function that takes a list as an argument and reverses its elements, in place. That is, mutate the list passed into the function. The returned object should be the same object used as the argument.

# You may not use the list.reverse method nor may you use a slice ([::-1]).

# list1 = [1, 2, 3, 4]
# result = reverse_list(list1)
# print(result == [4, 3, 2, 1])               # True
# print(list1 is result)                      # True

# list2 = ["a", "b", "c", "d", "e"]
# result2 = reverse_list(list2)
# print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
# print(list2 is result2)                     # True

# list3 = ["abc"]
# result3 = reverse_list(list3)
# print(result3 == ['abc'])                   # True
# print(list3 is result3)                     # True

# list4 = []
# result4 = reverse_list(list4)
# print(result4 == [])                        # True
# print(list4 is result4)                     # True

"""
P
input = a list
output = the same list, reversed
explicit = we can't use the .reverse method or slicing
implicit = if a list has one element or is empty, the list looks the same

E
# list5 = ["apples", "grapes", "bananas"]
# result5 = reverse_list(list5)
# print(result5 == ["bananas", "grapes", "apples"])     # True
# print(list5 is result5)                     # True

D
loops

A
(using LS's answer as it is way more succinct)
-we will assign index values to their respective variable names
-we'll use a while loop to iterate through only half of the length of the list
-we'll reassign the first and the last elements to the last and the first, respectively
-we'll increment + 1 to the first index
-we'll decrement -1 to the last index
-return the same list

C
"""
def reverse_list(lst):
    first = 0
    last = -1

    while first < (len(lst) // 2):
        lst[first], lst[last] = lst[last], lst[first]
        first += 1
        last -= 1

    return lst

list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True

list5 = ["apples", "grapes", "bananas"]
result5 = reverse_list(list5)
print(result5 == ["bananas", "grapes", "apples"])     # True
print(list5 is result5)                     # True