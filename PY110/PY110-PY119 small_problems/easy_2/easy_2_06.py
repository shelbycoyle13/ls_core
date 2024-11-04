# Multiplicative Average
# Write a function that takes a list of positive integers as input, multiplies all of the integers together, divides the result by the number of entries in the list, and returns the result as a string with the value rounded to three decimal places.

# All of these examples should print True
# print(multiplicative_average([3, 5]) == "7.500")
# print(multiplicative_average([2, 5, 8]) == "26.667")
# print(multiplicative_average([2, 5]) == "5.000")
# print(multiplicative_average([1, 1, 1, 1]) == "0.250")
# print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")

# P
# input = list (of positive integers)
# output = string
# explicit = we multiply the integers together. then, divide by the number of integers. we need the value rounded to 3 decimal places. return as a string.
# Implicit = it appears that there are no empty lists. even if we have an even average with zeros, we still put 3 decimal places. we could potentially have a 0 in the list.

# E
# print(multiplicative_average([4, 0]) == "0.000")

# D
# lists, for loops

# A
# iterate through the list, with each new number, mulitply
# once we have the final product, divide by the length of the list
# now we have an average, we need to round to 3 decimal places
# turn this final number into a string

# C
def multiplicative_average(lst):
    
    product = 1
    for num in lst:
        product *= num
    result = product / len(lst)
    return f"{result:.3f}"

print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")
print(multiplicative_average([4, 0]) == "0.000")