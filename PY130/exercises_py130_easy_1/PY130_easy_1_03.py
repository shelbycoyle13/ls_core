# Product of Numbers
# Calculate the product of all numbers in a list using the reduce function.
from functools import reduce

numbers = [1, 2, 3, 4]

sum1 = reduce(lambda accum, num: accum * num , numbers)

print(sum1)

#LS Solution 1
# from functools import reduce

# product = reduce(lambda x, y: x * y, [1, 2, 3, 4])

#LS Solution 2
# from functools import reduce

# def multiply(x, y):
#     return x * y

# product = reduce(multiply, [1, 2, 3, 4])