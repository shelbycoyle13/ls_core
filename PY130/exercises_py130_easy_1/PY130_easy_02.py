# Even Numbers
# Obtain only the even numbers from a list using the filter function.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_list = list(filter(lambda num: num % 2 == 0, numbers))

print(even_list)

# LS Solution 1

# even_numbers = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))

# LS Solution 2

# def is_even(x):
#     return x % 2 == 0

# even_numbers = list(filter(is_even, [1, 2, 3, 4, 5, 6]))