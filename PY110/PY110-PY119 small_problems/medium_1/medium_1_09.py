# Our recursive fibonacci function from the previous exercise isn't very efficient. It starts slowing down with an nth argument value somewhere around 35-60, depending on your system. One way to improve the performance of our recursive fibonacci function (and other recursive functions) is to use memoization.

# Memoization is an approach that involves saving a computed answer for future reuse, instead of computing it from scratch every time it is needed. In the case of our recursive fibonacci function, using memoization saves calls to fibonacci(nth - 2) because the necessary values have already been computed by the recursive calls to fibonacci(nth - 1).

# For this exercise, your objective is to refactor the recursive fibonacci function to use memoization.

# An image representing the computation of the 7th Fibonacci number is shown below. It is the same image that was shown in the previous exercise, except this one highlights the values that have previously been computed.

# Hint: One approach to memoization is to use a lookup table, such as an object, for storing and accessing previously computed values.

"""
P
input = integer
output = integer (sum of the current and previous integer)
explicit = we want to use another object to store the values of the previously computed values
implicit = 

E

D
dictionary

A
-initialize an empty dictionary
-if n is 1 or 2
    -return 1
-else if n is in the dictionary
    -return the value
-else
    dictionary[n] = fibonacci(n - 1) + fibonacci(n - 2)
    -return dictionary[n]

C
"""

lookup_dict = {}

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n in lookup_dict:
        return lookup_dict[n]
    else:
        lookup_dict[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return lookup_dict[n]
    
print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True