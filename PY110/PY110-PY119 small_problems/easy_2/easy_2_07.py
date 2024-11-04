# Multiply Lists
# Write a function that takes two list arguments, each containing a list of numbers, and returns a new list that contains the product of each pair of numbers from the arguments that have the same index. You may assume that the arguments contain the same number of elements.

# list1 = [3, 5, 7]
# list2 = [9, 10, 11]
# print(multiply_list(list1, list2) == [27, 50, 77])  # True

# P
# input = two lists
# output = one new list
# explicit = each new number represents the product of the two elements at the same index in each list). lists will have the same number of elements.
# Implicit = 0 could be a possibility of a number in the list

# E
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# print(multiply_list(list1, list2) == [4, 10, 18])  # True

# D
# lists, for loop

# A
# we could pair each element at the same index together
# for each pair, multiply the elements together to get a product
# add these products to a new list
# return the new list

# C

def multiply_list(lista, listb):
    zipped_list = list(zip(lista, listb))
    final_list = []
    
    for tup in zipped_list:
        product = 1
        for num in tup:
            product *= num
        final_list.append(product)
    return final_list

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# print(multiply_list(list1, list2) == [4, 10, 18])  # True