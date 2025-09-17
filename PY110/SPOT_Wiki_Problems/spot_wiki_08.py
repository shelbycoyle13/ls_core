# Smallest Substring Repeat

# Write a function that takes a non-empty string `s` as input and finds the minimum substring `t` and the maximum number `k`, such that the entire string `s` is equal to `t` repeated `k` times.

# Examples:
# f("ababab") # should return ["ab", 3]

"""
P
input = a string
output = a substring, and an integer; the substring X the integer = the original string
explicit = we need to find the minimum substring and the amount of times the substring repeats itself in the string
implicit = 

E

D
string
loop

A
-to make the code easier to read, we'll initialize variable n as the length of the string
-for i in range (1 to the length of the string + 1) #Starting at 1 helps begin the search for substrings!
    -if the length of the string is evenly divisible by the current index
        -then we have a possible substring, we're going to take a slice of the string[:i]
        -if the substring X (length of the string // the current index) is the same as the original string
            -return the substring, length of the string // index

C
"""

def f(string):

    n = len(string)

    for i in range(1, n + 1):
        if n % i == 0:  # If the length of the string is evenly divisible by the current index
            t = string[:i]  # We have a candidate substring
            if t * (n // i) == string:  # Check if repeating the candidate forms the original string. If it does:
                return [t, n // i]  # Return the substring and repetition count

# Test Case
print(f("ababab")) # should return ["ab", 3]
print(f("abcabcabc"))  # Output: ["abc", 3]