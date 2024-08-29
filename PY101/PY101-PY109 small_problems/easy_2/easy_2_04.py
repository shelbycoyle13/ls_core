# Using the multiply function from the "Multiplying Two Numbers" exercise, write a function that computes the square of its argument (the square is the result of multiplying a number by itself).

def multiply(arg1, arg2):
    return arg1 * arg2

def square(num1):
    return multiply(num1, num1)

# print(square(5) == 25)   # True
# print(square(-8) == 64)  # True

# Further Exploration
# Suppose we want to generalize this function to a "power to the n" type function: cubed, to the 4th power, to the 5th, etc. How would we go about doing so while still using the multiply function?

def power(num1, n):
    return multiply(num1, 1) ** n

print(power(8, 3))