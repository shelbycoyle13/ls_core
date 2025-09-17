# In the previous exercise, you wrote a function that transposed a 3x3 matrix represented by a list of lists.

# Matrix transposes are not limited to 3x3 matrices, or even square matrices. Any matrix can be transposed simply by switching columns with rows.

# Modify your transpose function from the previous exercise so that it works with any MxN matrix with at least one row and one column.

# All of these examples should print True
# print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
# print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
# print(transpose([[1]]) == [[1]])

# matrix_3_by_5 = [
#     [1, 2, 3, 4, 5],
#     [4, 3, 2, 1, 0],
#     [3, 7, 8, 6, 2],
# ]
# expected_result = [
#     [1, 4, 3],
#     [2, 3, 7],
#     [3, 2, 8],
#     [4, 1, 6],
#     [5, 0, 2],
# ]

# print(transpose(matrix_3_by_5) == expected_result)

"""
P
input = a nested list
output = a new nested list (lists have the numbers from the "columns")
explicit = we want to be able to take a list of at least 1 "row" and one "column" and use it with any matrix
implicit = 

E

D
lists

A
-for every row in the unpacked, zipped lst
    -turn the tuples into lists with the list constructor function

C
"""

def transpose(lst):
    return [list(row) for row in zip(*lst)] #Saving a step here by taking the matrix / outer lst and already using zip on in to place iterables in tuples. Then, just coerce the tuples into lists. Done!

    #LS Answer: The same answer from the previous exercise works. It appends the same amount of empty sublists as there are elements in each sublist. Then, one by one, adds each element to each sublist until there are no more elements to go through.
    # def transpose(matrix):
    # transposed = []
    # new_rows_count = len(matrix[0])

    # for _ in range(new_rows_count):
    #     transposed.append([])

    # for row_idx in range(len(matrix)):
    #     for col_idx in range(len(matrix[row_idx])):
    #         transposed[col_idx].append(matrix[row_idx][col_idx])

    # return transposed
        
print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
print(transpose([[1]]) == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)