# In the previous exercise, we developed a procedural solution for computing the nth Fibonacci number.

# This sequence can also be computed using a recursive function. A recursive function is one in which the function calls itself. For example, the following function is a recursive function that computes the sum of all integers between 1 and n:

# def sum_recursive(n):
#     if n == 1:
#         return 1

#     return n + sum_recursive(n - 1)

# Recursive functions are a bit difficult to understand for novice programmers, but it's worth putting in a little time early on to see what recursion looks like. Recursion can, in some situations, greatly simplify some algorithms.

# A recursive function has three primary qualities:

# It must have a base case. This is a condition that tells the function to stop recursing and begin the process of returning to the first call to the function. This is often the simplest case - the condition for which you already know the answer. In sum_recursive, the base case occurs when n == 1. At this point, we know the answer: sum_recursive(1) == 1. Thus, we can return the value 1.
# The function must call itself except when handling the base case.
# Each recursive call must be "closer" to the base case than the current call. For instance, in sum_recursive(3), we call sum_recursive(2), which is closer to the base case. Likewise, sum_recursive(2) subsequently calls sum_recursive(1), which is the base case.
# You may recall from the previous exercise that the Fibonacci sequence follows a simple set of rules:

# F(1) = 1
# F(2) = 1
# F(n) = F(n - 1) + F(n - 2)    (where n > 2)

# If you study this set of rules, you can see that the algorithm is defined recursively:

# The base case occurs when the argument is 1 or 2; both of these arguments result in a value of 1.
# The Fibonacci function calls itself. In fact, it calls itself twice.
# Except when dealing with the base case, each call to the Fibonacci function comes closer to the base case. In this case, both F(n - 1) and F(n - 2) are closer to the base case than F(n).
# Given this recursive algorithm, try to write a recursive function that computes the nth Fibonacci number, where nth is an argument passed to the function.

# This exercise borders on the Advanced level of exercises, so do not be discouraged if you are unable to solve it on your own. Recursion is tricky, and even experienced developers can have difficulty dealing with it. However, the practice is worthwhile; recursion plays a huge part in many algorithms.

# print(fibonacci(1) == 1)         # True
# print(fibonacci(2) == 1)         # True
# print(fibonacci(3) == 2)         # True
# print(fibonacci(4) == 3)         # True
# print(fibonacci(5) == 5)         # True
# print(fibonacci(6) == 8)         # True
# print(fibonacci(12) == 144)      # True
# print(fibonacci(20) == 6765)     # True

"""
P
input = integer
output = integer (the sum of the last two integers combined)
explicit = we want to follow the rules of a recursive function and turn the fibonacci function recursive
implicit = 

E

D

A
-as our base cases, if n is equal to either 1 or 2, return 1. else, let's call the fibonacci function again. We can use the forumla that was given to us.

C
"""

def fibonacci(n):

    if n == 1 or n == 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True