# Write a function that computes the difference between the square of the sum of the first count positive integers and the sum of the squares of the first count positive integers.

# print(sum_square_difference(3) == 22)          # True
# # 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

# print(sum_square_difference(10) == 2640)       # True
# print(sum_square_difference(1) == 0)           # True
# print(sum_square_difference(100) == 25164150)  # True

"""
P
input = integer (we go up to this number)
output = integer (difference between square of sum and sum of squares)
explicit = first calculate square of sums, then calculate sum of squares, calculate difference between the two
implicit = we're always starting at 1 in the sums

E


D
range

A
-initialize total at 0
-for num in range of 1 to the argument
    add to total

-initialize second total at 0
-for num in range of 1 to the argument
    -square the number and add to the total

-subtract the second total from the first
-return difference

C
"""
def sum_square_difference(arg1):
    first_total = 0

    for num in range(1, arg1 + 1):
        first_total += num

    first_total_squared = first_total**2

    second_total = 0

    for num in range(1, arg1 + 1):
        second_total += num**2
    
    return first_total_squared - second_total

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True

#More recent and more simple answer:

# def sum_square_difference(num):

#     list_of_nums = [i for i in range(1, num + 1)]

#     sum_squared = sum(list_of_nums)**2

#     sum_of_squares = 0

#     for num in list_of_nums:
#         sum_of_squares += num**2

#     difference = sum_squared - sum_of_squares

#     return difference