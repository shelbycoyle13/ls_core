# Square Numbers
# Create a list where each number from the original list is squared using the map method.
numbers = [1, 2, 3, 4, 5]

squared_list = list(map(lambda num: num ** 2, numbers))

print(squared_list)

# LS Solutions:

#Solution #1

# original_list = [1, 2, 3, 4]
# squared_numbers = list(map(lambda x: x**2, original_list))

# Solution 2 (defines the function to reuse elsewhere again)

# def square(x):
#     return x ** 2

# original_list = [1, 2, 3, 4]
# squared_numbers = list(map(lambda x: x**2, original_list))