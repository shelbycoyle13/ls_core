# A Rational Number is any number that can be represented as the result of the division between two integers, e.g., 1/3, 3/2, 22/7, etc. The number to the left is called the numerator, and the number to the right is called the denominator.

# A Unit Fraction is a rational number where the numerator is 1.

# An Egyptian Fraction is the sum of a series of distinct unit fractions (no two are the same), such as:

# Every positive rational number can be written as an Egyptian fraction. For example:

# Write two functions: one that takes a Rational number as an argument, and returns a list of the denominators that are part of an Egyptian Fraction representation of the number, and another that takes a list of numbers in the same format, and calculates the resulting Rational number. You will need to use the Fraction class provided by the fractions module.

# from fractions import Fraction

# # Using the egyptian function
# # Your results may differ for these first 3 examples
# print(egyptian(Fraction(2, 1)))      # [1, 2, 3, 6]
# print(egyptian(Fraction(137, 60)))   # [1, 2, 3, 4, 5]
# print(egyptian(Fraction(3, 1)))
# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 230, 57960]

# # Using the unegyptian function
# # All of these examples should print True
# print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
# print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
# print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
# print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
# print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
# print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
# print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
# print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))

# Every rational number can be expressed as an Egyptian Fraction. In fact, every rational number can be expressed as an Egyptian Fraction in an infinite number of different ways. Thus, the first group of examples may not show the same values as your solution. They do, however, show the expected form of the solution. The remaining examples merely demonstrate that the output of egyptian can be reversed by unegyptian.

# Note that the techniques for calculating Egyptian Fractions shown on the Wikipedia page may not be the easiest to understand or implement -- the algorithms described there are generally meant to arrive at a solution as quickly as possible or to arrive at a specific solution (such as the shortest solution). Feel free to use a simpler approach: check whether 1 / 1 can be part of the solution, then 1 / 2, then 1 / 3, then 1 / 4, and so on. This is relatively easy to implement compared to some other techniques.

"""
P
input = two numbers which represent a fraction, the first number is the numerator, the second is the denominator
output = a list of denominators which represent its Egyptian numbers
explicit = we must make two functions, one that takes a rational numbers and gives a list of the denominators of its egyptian numbers; the other function takes the list of denominators of its egyptian numbers and returns the rational number
implicit = 

E

D
list

A
(to change the rational number into a list of denominators)
-initialize an empty list to keep track of the denominators
-the unit denominator will always start at one (i,e. 1/1)
-while the target value (our argument) is not equal to 0
    - the unit fraction will equal Fraction(1, unit_denominator) (this is just using the fractions module to convert our two integer arguments to a fraction)
    - if the unit_fraction that we just calculated is less than or equal to the target value we need
        - the target value will subtract the unit_fraction that was calculated for this iteration
        - we then want to append the unit_denominator to the denominators list
    -add 1 to the unit_denominators
-return the denominators list

(to change the list of denominators back into a rational number)
-for every integer in the denominators list
    -use the Fractions class(1, integer)
-return the sum of what is in this list (i.e. we're adding all of the egyptian fractions here to make a rational number, aka a fraction)

C
"""

from fractions import Fraction

def egyptian(target_value):
    denominators = []
    unit_denominator = 1
    while target_value != 0:
        unit_fraction = Fraction(1, unit_denominator)
        if unit_fraction <= target_value:
            target_value -= unit_fraction
            denominators.append(unit_denominator)

        unit_denominator += 1

    return denominators

def unegyptian(denominators):
    print(sum([Fraction(1, d) for d in denominators]))

from fractions import Fraction

# Using the egyptian function
# Your results may differ for these first 3 examples
print(egyptian(Fraction(2, 1)))      # [1, 2, 3, 6]
print(egyptian(Fraction(137, 60)))   # [1, 2, 3, 4, 5]
print(egyptian(Fraction(3, 1)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 230, 57960]

# Using the unegyptian function
# All of these examples should print True
print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))