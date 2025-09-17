# 18. Multiplicative Persistence
# Write a function, persistence, that takes in a positive parameter
# `num` and returns its multiplicative persistence, which is the number
# of times you must multiply the digits in `num` until you reach a single digit.

# Examples:
# persistence(39) # should return 3, because 3*9=27, 2*7=14, 1*4=4
# # and 4 has only one digit
# persistence(999) # should return 4, because 9*9*9=729, 7*2*9=126,
# # 1*2*6=12, and finally 1*2=2
# persistence(4) # should return 0, because 4 is already a one-digit number
# persistence(25) # should return 2, because 2*5=10, and 1*0=0

"""
P
input = a number
output = an integer
explicit = we must return the number of times the numbers in the argument multiplied by each other returns just a single digit
implicit = 

E

D
strings

A
-coerce the number to a string
-product = 1
count = 0

-while len(product) > 1:
    -for digit in string
        -product *= int(digit)
        -count += 1

-return count

C
"""

def persistence(num):
    
    count = 0

    while num >= 10: #If a number is not greater than or = to 10, that means its a single digit, which is what we want
        product = 1 #Place product in loop to always reset to 1
        for digit in str(num):
            product *= int(digit)
        num = product  #We reassign num to product because this is the new number that we want to multiply the digits from. This will carry over onto the start of the loop
        count += 1

    return count

print(persistence(39) == 3) # should return 3, because 3*9=27, 2*7=14, 1*4=4
# # and 4 has only one digit
print(persistence(999) == 4) # should return 4, because 9*9*9=729, 7*2*9=126,
# # 1*2*6=12, and finally 1*2=2
print(persistence(4) == 0) # should return 0, because 4 is already a one-digit number
print(persistence(25) == 2) # should return 2, because 2*5=10, and 1*0=0