# A 3x3 matrix can be represented by a list of nested lists: an outer list that contains three sub-lists that each contain three elements. For example, the 3x3 matrix shown below:

# 1  5  8
# 4  7  2
# 3  9  6

# is represented by the following list of lists:

# matrix = [
#     [1, 5, 8],
#     [4, 7, 2],
#     [3, 9, 6],
# ]

# A list of lists is sometimes called a nested list since each inner sub-list is nested inside an outer list. It also may be called a two-dimensional list.

# To access an element in the matrix, you can use bracket notation twice (such as matrix[row][col]), and include both the row index and column index within the brackets. Given the above matrix, matrix[0][2] is 8, and matrix[2][1] is 9. An entire row in the matrix can be referenced using a single index: matrix[1] is the row (sub-list) [4, 7, 2]. Unfortunately, a convenient notation for accessing an entire column does not exist.

# The transpose of a 3x3 matrix is the matrix that results from exchanging the rows and columns of the original matrix. For example, the transposition of the matrix shown above is:

# 1  4  3
# 5  7  9
# 8  2  6

# Write a function that takes a list of lists that represents a 3x3 matrix and returns the transpose of the matrix. You should implement the function on your own, without using any external libraries.

# Take care not to modify the original matrix -- your function must produce a new matrix and leave the input matrix list unchanged.

# matrix = [
#     [1, 5, 8],
#     [4, 7, 2],
#     [3, 9, 6],
# ]

# new_matrix = transpose(matrix)

# print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
# print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True

"""
P
input = a nested list
output = a different nested list; we want to have the new sublists represent the "columns of the matrix"
explicit = we cannot use any external libraries
implicit = 

E
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6], 
#     [7, 8, 9],
# ]

# new_matrix = transpose(matrix)

# print(matrix == [[1, 2, 3], [4, 5, 6], [7, 8, 9]])     # True
# print(new_matrix == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]) # True


D
lists

A
-initialize a new outer list = []
-for sublist in lst
    -initialize 3 new sublists = []
    -for num in sublist:
        if num == sublist[0]:
            new_sublist1 += num
        elif num == sublist[1]
            new_sublist2 += num
        else:
            new_sublist3 += num
    new_outer_list += sublist

    return new outer_list


C
"""

def transpose(lst):    
    # new_outer_list = [[sublist[i] for sublist in lst] for i in range(len(lst[0]))]

    # OR def transpose(matrix: list):               # My favorite answer is using zip(unpacking the iterables in matrix) to put elements in each inner index in their own tuple
    # return([list(row) for row in zip(*matrix)]) #Then for every row/tuple in this list, return that row/tuple but coerced into a list

    # OR LS Answer:
        # def transpose(matrix):
        # transposed = []
        # new_rows_count = len(matrix[0]) #length of element 1 = 3

        # for _ in range(new_rows_count): #For every element in range 3
        #     transposed.append([]) #Append an empty list

        # for row_idx in range(len(matrix)): #For every row in range 3
        #     for col_idx in range(len(matrix[row_idx])): #For every column in range 0-2
        #         transposed[col_idx].append(matrix[row_idx][col_idx]) #At the outer list[column index], (so for each sublist),
                                    # we want to append each element in the first sublist to their own sublist. The next sublist elements will be added to the previous 3 sublists, one in each. Same for the last iteration.

        # return transposed

    sublist1 = [num for sublist in lst
                      for num in sublist
                      if num == sublist[0]
                      ]
    sublist2 = [num for sublist in lst
                      for num in sublist
                      if num == sublist[1]
                      ]

    sublist3 = [num for sublist in lst
                      for num in sublist
                      if num == sublist[2]
                      ]

    new_outer_list = [sublist1, sublist2, sublist3]
    return new_outer_list    

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True