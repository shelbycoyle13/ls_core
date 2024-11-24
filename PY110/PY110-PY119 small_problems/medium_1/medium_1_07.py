# The Fibonacci series is a sequence of numbers in which each number is the sum of the previous two numbers. The first two Fibonacci numbers are 1 and 1. The third number is 1 + 1 = 2, the fourth is 1 + 2 = 3, the fifth is 2 + 3 = 5, the sixth is 3 + 5 = 8, and so on. In mathematical terms, this can be represented as:

# F(1) = 1
# F(2) = 1
# F(n) = F(n - 1) + F(n - 2)    (where n > 2)

# Write a function called fibonacci that computes the nth Fibonacci number, where nth is an argument passed to the function:

# print(fibonacci(1) == 1)                  # True
# print(fibonacci(2) == 1)                  # True
# print(fibonacci(3) == 2)                  # True
# print(fibonacci(4) == 3)                  # True
# print(fibonacci(5) == 5)                  # True
# print(fibonacci(6) == 8)                  # True
# print(fibonacci(12) == 144)               # True
# print(fibonacci(20) == 6765)              # True
# print(fibonacci(50) == 12586269025)       # True
# print(fibonacci(75) == 2111485077978050)  # True

"""
P
input = integer
output = integer (the nth number in the sequence)
explicit = the nth number in the sequence is the result of the current element and the previous one in the sequence
implicit = 

E
[1, 1, 2, 3, 5, 8, 13]

D
list

A
#Using LS' answer:
-first we will assign the previous number in the iteration to 1 as that is the first number in the sequence
-the current number in the sequence is 1, so we will initialize "current" variable with that
-since the fibonacci series starts with 1, 1 by default, and doesn't start adding number until we get to the third number, let's make a guard clause to just return 1 if the argument is either 1 or 2
-we do want to iterate through a range of numbers
    -we want to start our iteration at the third number
    -and up to and including the argument we are given
    -as we iterate through the range, we are going to reassign the previous number to the current number, and the current number will be reassigned to the current number plus the previous
-return the current number

C
"""

def fibonacci(n):
    previous, current = 1, 1 #notice here we're not even using any data structures. Yes this is an option!

    if n == 1 or n == 2: #guard clause if argument is 1 or 2, we still return 1 since we don't start adding numbers until the 3rd number
        return 1

    for _ in range(3, n + 1): #we're starting our iteration at the 3rd number and going up to and including the argument. why? because we're not iterating through indexes this time. we want to go up to and include the the nth element or else we'll be 1 short
        previous, current = current, previous + current #here we are just reassigning. the previous number now equals the current. The current number now equals the current plus the previous

    return current
        
print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True