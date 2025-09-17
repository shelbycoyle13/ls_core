# As we saw in the previous exercises, a matrix can be represented by a list of lists. For example, the 3x3 matrix shown below:

# 1  5  8
# 4  7  2
# 3  9  6

# is represented by the following list of list:

# matrix = [
#     [1, 5, 8],
#     [4, 7, 2],
#     [3, 9, 6],
# ]

# A 90-degree rotation of a matrix produces a new matrix in which each side of the matrix is rotated clockwise by 90 degrees. For example, the 90-degree rotation of the matrix shown above is:

# 3  4  1
# 9  7  5
# 6  2  8

# A 90-degree rotation of a non-square matrix is similar. For example, given the following matrix:

# 3  4  1
# 9  7  5

# its 90-degree rotation is:

# 9  3
# 7  4
# 5  1

# Write a function that takes an arbitrary MxN matrix, rotates it clockwise by 90-degrees as described above, and returns the result as a new matrix. The function should not mutate the original matrix.

# matrix1 = [
#     [1, 5, 8],
#     [4, 7, 2],
#     [3, 9, 6],
# ]

# matrix2 = [
#     [3, 7, 4, 2],
#     [5, 1, 0, 8],
# ]

# new_matrix1 = rotate90(matrix1)
# new_matrix2 = rotate90(matrix2)
# new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# # These examples should all print True
# print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
# print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
# print(new_matrix3 == matrix2)

"""
P
input = a list
output = a new list
explicit = we want to "rotate" the matrix by 90 degrees clockwise, so visually it looks like we are taking the columns making that the new rows (but the numbers are in reverse, bottom to top, left to right)
implicit = number of new lists will be the same as the number of integers in original list

E
# matrix4 = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
# ]
# print(new_matrix2 == [[5, 1], [6, 2], [7, 3], [8, 4]])

D
lists

A
-for every row in the zipped iterables in the given list
    -coerce the tuples back into a list
    -reverse the list elements
-return the new list

C
"""
def rotate90(lst):
    rows_to_columns = [list(row) for row in zip(*lst)]

    for sublist in rows_to_columns:
        sublist.reverse()
    return rows_to_columns

    #LS Answer:
    # def rotate90(matrix):
    # rotated = []
    # new_rows_count = len(matrix[0])

    # for _ in range(new_rows_count):
    #     rotated.append([])

    # for row_idx in range(len(matrix)):
    #     for col_idx in range(len(matrix[row_idx])):
    #         rotated[col_idx].append(matrix[row_idx][col_idx])

    # for row in rotated: #Identical to the previous answer, with the addition of iterating through the list and reversing the contents
    #     row.reverse()

    # return rotated

matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

matrix4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))
new_matrix4 = rotate90(matrix4)

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)
print(new_matrix4 == [[5, 1], [6, 2], [7, 3], [8, 4]])