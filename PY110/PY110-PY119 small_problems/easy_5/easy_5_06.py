# Write a function that takes a list of numbers and returns the sum of the sums of each leading subsequence in that list. Examine the examples to see what we mean. You may assume that the list always contains at least one number.

# print(sum_of_sums([3, 5, 2]) == 21)               # True
# # (3) + (3 + 5) + (3 + 5 + 2) --> 21

# print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# # (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

# print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# # (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

# print(sum_of_sums([4]) == 4)                      # True

"""
P
input = a list of integers
output = one integer (sum of each leading sequence)
explicit = we're always returning a list with at least one number in it
implicit = 

E
# print(sum_of_sums([1, 2, 3]) == 10)               # True
# # (1) + (1 + 2) + (1 + 2 + 3) --> 10
1 = lst[0]
1 and 2 = lst[0] and lst[1]
1 and 2 and 3 = lst[0] and lst[1] and lst[2]

D
lists

A
-initialize a total sum
-initialize a running sum
-for num in list
    add num to the running sum
    add the running sum to the total sum
-return the total sum

C
"""

def sum_of_sums(lst):
    total_sum = 0
    running_sum = 0
    for num in lst:
        running_sum += num
        total_sum += running_sum
    return total_sum

print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True

print(sum_of_sums([1, 2, 3]) == 10)               # True
# (1) + (1 + 2) + (1 + 2 + 3) --> 10