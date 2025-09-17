# A triangle is classified as follows:

# Equilateral: All three sides have the same length.
# Isosceles: Two sides have the same length, while the third is different.
# Scalene: All three sides have different lengths.
# To be a valid triangle, the sum of the lengths of the two shortest sides must be greater than the length of the longest side, and every side must have a length greater than 0. If either of these conditions is not satisfied, the triangle is invalid.

# Write a function that takes the lengths of the three sides of a triangle as arguments and returns one of the following four strings representing the triangle's classification: 'equilateral', 'isosceles', 'scalene', or 'invalid'.

# print(triangle(3, 3, 3) == "equilateral")  # True
# print(triangle(3, 3, 1.5) == "isosceles")  # True
# print(triangle(3, 4, 5) == "scalene")      # True
# print(triangle(0, 3, 3) == "invalid")      # True
# print(triangle(3, 1, 1) == "invalid")      # True

"""
P
input = 3 integers
output = a string
explicit = the two smaller integers summed must be greater in value than the greatest integer to be a valid triangle
implicit - the arguments can be floats or 0. we can't have negative numbers

E
# print(triangle(5, 5, 3) == "isosceles")  # True

D
list

A
-initialize a list that has all 3 of the argument
- sort by smallest to largest

-for each integer in the lst
    -if arg1 + arg2 <= arg3:
        return "Invalid"
    else:
        -if all 3 arguments are the same:
            -return "Equilateral"
        -else if 2 arguments are the same"
            -return "Isosceles"
        -else:
            -return "Scalene"

C
"""

def triangle(arg1, arg2, arg3):
    lst = [arg1, arg2, arg3]
    lst.sort()

    
    if lst[0] + lst[1] <= lst[2]:
        return "invalid"
    else:
        if lst[0] == lst[1] == lst[2]:
            return "equilateral"
        elif lst[0] == lst[1] or lst[0] == lst[2] or lst[1] == lst[2]:
            return "isosceles"
        else:
            return "scalene"
            
print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True
print(triangle(5, 5, 3) == "isosceles")  # True     

#Second, similar, more readable answer:

def triangle(side1, side2, side3):
    lst = [side1, side2, side3]
    lst.sort()

    if sum(lst[:2]) <= lst[2]:
        return "invalid"
        
    if lst[0] == lst[1] == lst[2]:
            return "equilateral"
    
    for side in lst:
        if lst.count(side) == 2:
             return "isosceles"
    
    return "scalene"