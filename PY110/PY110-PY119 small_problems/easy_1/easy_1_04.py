# Running Totals

# Write a function that takes a list of numbers and returns a list with the same number of elements, but with each element's value being the running total from the original list.

# print(running_total([2, 5, 13]) == [2, 7, 20])    # True
# print(running_total([14, 11, 7, 15, 20])
#       == [14, 25, 32, 47, 67])                    # True
# print(running_total([3]) == [3])                  # True
# print(running_total([]) == [])                    # True

# P 
# input = list of integers
# output = list of integers, but each element is replaced with the sum with the element before it
# explicit = we add the current element with the one before it. replace the current element with the new sum
# implicit = We can have any number of elements including 1 or 0 elements

# E
# Examples / test cases are above

# D
# Lists

# A
# - We start with the first element of the list. No need to compute the sum, just add the first number to the new list.
# - On the next iteration, take the previous element and add with the current element. Compute the sum.
# - Replace the current element with the sum you just computed.
# - Repeat until you run out of elements.

# C

def running_total(list):
    new_list = []

    for index, number in enumerate(list):
        if list == []:
            return new_list
        if index == 0:
            new_list.append(number)
        else:
            new_list.append(new_list[index - 1] + number)
    return new_list

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True