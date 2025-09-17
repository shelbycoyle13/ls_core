# A featured number (something unique to this exercise) is an odd number that is a multiple of 7, with all of its digits occurring exactly once each. For example, 49 is a featured number, but 98 is not (it is not odd), 97 is not (it is not a multiple of 7), and 133 is not (the digit 3 appears twice).

# Write a function that takes an integer as an argument and returns the next featured number greater than the integer. Issue an error message if there is no next featured number.

#Note: The largest possible featured number is 9876543201.

# print(next_featured(12) == 21)                  # True
# print(next_featured(20) == 21)                  # True
# print(next_featured(21) == 35)                  # True
# print(next_featured(997) == 1029)               # True
# print(next_featured(1029) == 1043)              # True
# print(next_featured(999999) == 1023547)         # True
# print(next_featured(999999987) == 1023456987)   # True
# print(next_featured(9876543186) == 9876543201)  # True
# print(next_featured(9876543200) == 9876543201)  # True

# error = ("There is no possible number that "
#          "fulfills those requirements.")
# print(next_featured(9876543201) == error)       # True

"""
P
input = integer
output = integer (featured numer = a multiple of 7, with all digits occurring exactly once, also an odd number)
explicit = return the next featured number
implicit = 

E

D
list

A
-first let's create a helper function that checks to make sure a number is odd and divisible by 7
    -we want to skip checking the actual number because we want the NEXT featured number, so we'll increment the number right from the beginning
    -while the number is even and not divisible by 7
        -increment the number
    -once the while loop finds a number that satisfies both
    -return that number
-let's also create a helper function to make sure all of the digits in a number are unique
    -the digits in a number are going to equal the number coerced into a string, which will then be placed into a list using the list constructor function
    -if the lenth of the digits are the same as the length of the set of digits, return True (we use a set constructor on digits because we only want unique digits from the number)
-finally, we have our main next_featured function
    - we'll set a max constant number (we are given this number)
    - the featured_number is going to be equal to the return value of passing in the object referenced by number to odd_multiples_of_7
    - while the featured_number if less than or equal to the max featured number
        -if the return value of passing in the featured number to the all_unique function is True:
            -return the featured number
        -we will add 14 to the featured number in each iteration because 14 is a good way to go to the next divisible number of 7 that is odd
        else if we haven't returned the featured number by now, return the error message
C
"""
def odd_multiple_of_7(number):
    number += 1
    while number % 2 == 0 or number % 7 != 0:
        number += 1

    return number

def all_unique(number):
    digits = list(str(number))
    return len(digits) == len(set(digits))

def next_featured(number):
    MAX_FEATURED = 9876543201
    featured_num = odd_multiple_of_7(number)

    while featured_num <= MAX_FEATURED:
        if all_unique(featured_num):
            return featured_num

        featured_num += 14

    return "There is no possible number that fulfills those requirements."

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True