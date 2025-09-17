# Problem 14
# Create a function that takes a single integer argument and returns the sum of all the multiples of 7 or 11 that are less than the argument. If a number is a multiple of both 7 and 11, count it just once.

# For example, the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21, and 22. The sum of these multiples is 75.

# If the argument is negative, return 0.

# The below tests should each print True.

# print(seven_eleven(10) == 7)
# print(seven_eleven(11) == 7)
# print(seven_eleven(12) == 18)
# print(seven_eleven(25) == 75)
# print(seven_eleven(100) == 1153)
# print(seven_eleven(0) == 0)
# print(seven_eleven(-100) == 0)

"""
P
input = an integer
output = an integer
explicit = we want to return the sum of all the multiples of 7 or 11 that are LESS than the argument. if a number if a multiple of 7 or 11, count it just once. if a number is less than 0, return 0.
implicit = 

E

D
range
list

A
-initialize empty multiples list
-if a number is less than 0, return 0
-else
    -we want to iterate in a range up to the argument
        -if the index % 7 == 0 or argument % 11 == 0:
            -append to multiples list
    -return the sum of the multiples list

C
"""
def seven_eleven(number):
    multiples = []

    if number < 0:
        return 0
    else:
        for i in range(number):
            if i % 7 == 0 or i % 11 == 0:
                multiples.append(i)
    
    return sum(multiples)

print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)

# Second answer, almost identical, but better variable naming, easier to understand
# def seven_eleven(num):

#     if num <= 0:
#         return 0
        
#     multiples = []

#     for multiple in range(num):
#         if multiple % 7 == 0 or multiple % 11 == 0:
#             multiples.append(multiple)
    
#     return sum(multiples)