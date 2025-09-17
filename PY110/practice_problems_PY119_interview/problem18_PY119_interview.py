# Problem 18
# Create a function that takes a list of integers as an argument. Determine and return the index N for which all numbers with an index less than N sum to the same value as the numbers with an index greater than N. If there is no index that would make this happen, return -1.

# If you are given a list with multiple answers, return the index with the smallest value.

# The sum of the numbers to the left of index 0 is 0. Likewise, the sum of the numbers to the right of the last element is 0.

# The below tests should each print True.

# print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
# print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
# print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
# print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# # The following test case could return 0 or 3. Since we're
# # supposed to return the smallest correct index, the correct
# # return value is 0.
# print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)

"""
P
input = a list (of integers)
output = an integer (represents the index)
explicit = we want to return the index in which all of the integers summed up less than that integer have the same sum as the integers after that same index. we want to return the smallest integer if there's more than 1 correct answer. if this is not possible, return -1.
implicit = 

E

D
list

A
-iterate through the list, for i, num in enumerate(lst)
    -if sum(range(i)) == sum(range(i + 1, len(lst)))
        -return index

    return -1

C
"""
def equal_sum_index(lst):
    for i, num in enumerate(lst):
        if sum(lst[:i]) == sum(lst[i + 1:]):
            return i
    
    return -1

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)

#Second, probably cleaner answer:

def equal_sum_index(lst):

    for i in range(len(lst)):
        if sum(lst[:i]) == sum(lst[i + 1:]):
            return i
    return -1