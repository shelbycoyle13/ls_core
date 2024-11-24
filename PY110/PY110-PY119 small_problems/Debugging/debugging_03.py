# You want to multiply all elements of a list by 2. However, the function is not returning the expected result. Explain the bug, and provide a solution.

# def multiply_list(lst):
#     for item in lst:
#         item *= 2 # Here we are triyng to multiply the element by 2

#     return lst #But we are returning the same exact list. "item" references an integer object that won't change the original list. We should return a new list.

# print(multiply_list([1, 2, 3]) == [2, 4, 6])

def multiply_list(lst):
    final_list = []
    for item in lst:
        final_list.append(item * 2)

    return final_list

print(multiply_list([1, 2, 3]))