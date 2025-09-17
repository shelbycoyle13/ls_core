# Odd Number Sub-strings
# Write a function that takes a string of integers as input and returns the number of substrings that result in an odd number when converted to an integer.

# Examples:
# solve("1341") # should return 7
# solve("1357") # should return 10

"""
P
input = a string (of integers)
output = an integer
explicit = we need to return the number of substrings that result in an odd number (when converted to an integer)
implicit = 

E

D
loops / comprehensions

A
-get the coerced integer substrings of the string by using a nested for loop or nested list comprehension
-initialze a count of 0
-if the "substring" is odd, add 1 to the count
-retun the count
C
"""

def solve(string):
    # count = 0

    # for i in range(len(string)): #This outer loop is getting the start index of the slice. It also sets how many iterations the entire loop will run (4 times)
    #     for j in range(i + 1, len(string) + 1): #This inner loop is getting the stop index of the slice.
    #         if int(string[i:j]) % 2 == 1: #This checks for odd numbers
    #             count += 1 #If it's odd, incremement the count

    # return count

    count = sum([1 for i in range(len(string)) #Same thing as above, only for every odd number, we want 1, and we pass this entire comprehension into a sum function
             for j in range(i + 1, len(string) + 1)
             if int(string[i:j]) % 2 == 1])
    
    return count

print(solve("1341")) # should return 7
print(solve("1357")) # should return 10