# Write a function that takes a positive integer, n, as an argument and prints a right triangle whose sides each have n stars. The hypotenuse of the triangle (the diagonal side in the images below) should have one end at the lower-left of the triangle, and the other end at the upper-right.

def triangle(integer):
    for i in range(1,integer + 1):
        print(" " * (integer - i) + "*" * i)

triangle(5)

#     *
#    **
#   ***
#  ****
# *****