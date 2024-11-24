# Given two lists of integers of the same length, return a new list where each element is the product of the corresponding elements from the two lists.

# list_a = [1, 2, 3]
# list_b = [4, 5, 6]
# print(multiply_items(list_a, list_b) == [4, 10, 18]) # True

"""
P
input = two lists (of the same length)
output = one list (with the products of the previous lists)
explicit = multiple the integers from each list that have the same index
implicit = 

E
# list_a = [7, 8, 9]
# list_b = [0, 10, 11]
# print(multiply_items(list_a, list_b) == [0, 80, 99]) # True

D
lists

A
-use zip to combine elements of the same index
-initialize final list as empty
- for num1, num2 in long list
    - num1 * num2
    - append product to new list
-return new list

C
"""
def multiply_items(lst1, lst2):
    final_list = []

    long_list = list(zip(lst1, lst2))

    for num1, num2 in long_list:
        product = num1 * num2
        final_list.append(product)
    return final_list

    # return [num1 * num2 for num1, num2 in long_list]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True

list_a = [7, 8, 9]
list_b = [0, 10, 11]
print(multiply_items(list_a, list_b) == [0, 80, 99]) # True