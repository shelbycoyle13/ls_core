# Capture all the rest
# Unpack the first two elements from a list and store the remaining elements in another list.

numbers = [1, 2, 3, 4, 5, 6]

a, b, *c = numbers

print(a, b, c)