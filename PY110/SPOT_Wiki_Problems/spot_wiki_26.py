# 26. Mean Square
# # Create a function that takes two integer lists of equal length, compares the value of each member in one list to the corresponding member in the other, 
# # squares the absolute value difference between those two values, and returns the average of those squared absolute value differences between each member pair.

# # Examples
# # [1, 2, 3], [4, 5, 6] --> 9 because (9 + 9 + 9) / 3
# # [10, 20, 10, 2], [10, 25, 5, -2] --> 16.5 because (0 + 25 + 25 + 16) / 4
# # [-1, 0], [0, -1] --> 1 because (1 + 1) / 2

# p solution([1, 2, 3], [4, 5, 6]) == 9
# p solution([10, 20, 10, 2], [10, 25, 5, -2]) == 16.5
# p solution([-1, 0], [0, -1]) == 1

"""
P
input = two lists
output = one integer
explicit = we want to substract the number at their corresponding index. take the absolute value difference. square that. add those together. divide by the amount of numbers (to get the average)
implicit = 

E

D
lists

A
-initialize a new list to hold values of diffs
-iterate over the first list, for each index, num in list1
    -diffs.append(abs(list1[index] - list2[index]))

-initialize squared diffs list, set equal to num ** 2 for each num in diffs

-initialize sum of squares, set equal to summing the squared diffs list

-return sum // length of first list


C
"""
def solution(list1, list2):
    differences = []

    for index, num in enumerate(list1):
        differences.append(abs(list1[index] - list2[index]))

    squared_diffs = [num ** 2 for num in differences]
    
    sum_of_squares = sum(squared_diffs)

    return sum_of_squares / len(list1)

print(solution([1, 2, 3], [4, 5, 6]) == 9)
print(solution([10, 20, 10, 2], [10, 25, 5, -2]) == 16.5)
print(solution([-1, 0], [0, -1]) == 1)