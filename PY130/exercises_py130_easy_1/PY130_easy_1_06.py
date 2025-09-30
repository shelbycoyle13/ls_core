# Concatenate Strings
# Use reduce to concatenate a list of strings into a single string.

from functools import reduce

words = ["Is", "this", "the", "real", "life"]

one_string = reduce(lambda accum, x: accum + x, words)

print(one_string)

#LS Solution 1
# from functools import reduce

# concatenated = reduce(lambda x, y: x + y, ["Launch", " ", "School", " ", "is", " ", "great"])

#LS Solution 2
# from functools import reduce

# def concatenate(x, y):
#     return x + y

# concatenated = reduce(concatenate, ["Launch", " ", "School", " ", "is", " ", "great"])