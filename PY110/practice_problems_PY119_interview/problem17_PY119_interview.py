# Problem 17
# Create a function that takes a list of integers as an argument. The function should determine the minimum integer value that can be appended to the list so the sum of all the elements equal the closest prime number that is greater than the current sum of the numbers. For example, the numbers in [1, 2, 3] sum to 6. The nearest prime number greater than 6 is 7. Thus, we can add 1 to the list to sum to 7.

# Notes:

# The list will always contain at least 2 integers.
# All values in the list must be positive (> 0).
# There may be multiple occurrences of the various numbers in the list.

# The below tests should each print True.

"""
P
input = a list (of integers)
output = an integer
explicit = after getting the sum of the integers in the list, we need to return the integer that, when added to the current sum, would be equal to the next closest prime number
implicit = 

E


D
list

A
-we need a helper function to determine if a number is prime or not
-sum the integers in the list
-keep adding 1 to the sum, check if its a prime number (can only be divisible by itself and 1; 1 is not a prime number)
    -if it is, return the difference
    -else, keep adding 1

C
"""
def is_it_prime(num):

    if num < 2: # Number 1 and anything less is NOT a prime number
        return False
    
    for i in range(2, int(num**.5) + 1): # We start our range at 2, since 2 is the minimum prime number. Our stop number is the square root of our number, coerced down to the nearest integer, plus 1, since we want to include that number. A "trick" to using the square root is that for factors, you only need to check up to the square root of the number. No sense in checking anything higher. If it can be evenly divisible by any of the smaller numbers, then it's not prime anyway. 
        if num % i == 0:
            return False
    
    return True #If none of the factors are evenly divisble, then we've found a prime number

def nearest_prime_sum(lst):

    sum_of_list = sum(lst)

    next_greatest_prime = sum_of_list + 1

    while not is_it_prime(next_greatest_prime):
        next_greatest_prime += 1

    return next_greatest_prime - sum_of_list

print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)

#Second answer, almost the same, but more fleshed out

def is_it_prime(num):
    
    if num < 2:
        return False

    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    
    return True

def nearest_prime_sum(lst):
    
    sum1 = sum(lst)

    difference = 0

    sum2 = sum1 + 1

    difference += 1

    while not is_it_prime(sum2):
        sum2 += 1
        difference += 1

    return difference