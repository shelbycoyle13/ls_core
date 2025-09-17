# 21. Mine Location
# You've just discovered a square (NxN) field and you notice a warning sign.
# The sign states that there's a single bomb in the 2D grid-like field in front
# of you.

# Write a function `mine_location` that accepts a 2D array, and returns the
# location of the mine. The mine is represented as the integer 1 in the 2D array.
# Areas in the 2D array that are not the mine will be represented as 0s.

# The location returned should be an array where the first element is the row index, and the second element is the column index of the bomb location (both should be 0 based). All 2D arrays passed into your function will be square (NxN), and there will only be one mine in the array.

# Examples:
# mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) # should return [0, 0]
# mine_location([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) # should return [1, 1]
# mine_location([[0, 0, 0], [0, 0, 0], [0, 1, 0]]) # should return [2, 1]
# mine_location([[1, 0], [0, 0]]) # should return [0, 0]
# mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) # should return [0, 0]
# mine_location([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]) # should return [2, 2]

"""
P
input = lists
output = a list
explicit = the returned list will contain the row, column of where the #1 is located in the list arguments passed
implicit = 

E

D
lists

A
for i, sublist in enumerate(list)
    for j, num in enumerate(sublist)
        if num == 1
            return [i, j]

C
"""
def mine_location(lst):
    for i, sublist in enumerate(lst):
        for j, num in enumerate(sublist):
            if num == 1:
                return [i, j]

print(mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) == [0, 0]) # should return [0, 0]
print(mine_location([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == [1, 1])# should return [1, 1]
print(mine_location([[0, 0, 0], [0, 0, 0], [0, 1, 0]]) == [2, 1])# should return [2, 1]
print(mine_location([[1, 0], [0, 0]]) == [0, 0]) # should return [0, 0]
print(mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) == [0, 0])# should return [0, 0]
print(mine_location([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]) == [2, 2])# should return [2, 2]