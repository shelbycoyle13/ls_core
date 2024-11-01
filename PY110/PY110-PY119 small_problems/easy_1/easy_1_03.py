# Palindromic Strings (Part 2)
# Write another function that returns True if the string passed as an argument is a palindrome, or False otherwise. This time, however, your function should be case-insensitive, and should ignore all non-alphanumeric characters. If you wish, you may simplify things by calling the is_palindrome function you wrote in the previous exercise.

# print(is_real_palindrome('madam') == True)           # True
# print(is_real_palindrome('356653') == True)          # True
# print(is_real_palindrome('356635') == False)         # True
# print(is_real_palindrome('356a653') == True)         # True
# print(is_real_palindrome('123ab321') == False)       # True

# # case doesn't matter
# print(is_real_palindrome('Madam') == True)           # True

# # only alphanumerics matter
# print(is_real_palindrome("Madam, I'm Adam") == True) # True

# P 
# input = string
# output = Boolean
# explicit = We're passing in a string that can be any length, with any cases, and any characters. Case and characters DON'T matter.
# implicit = It doesn't appear we can have empty strings.

# E
# Examples / test cases are above

# D
# For loops, strings

# A
# - After receiving the string, we should split the string in half
# - if the length of the string is odd, include a halfway point
# - compare the string on the "left" with the string on the "right" but the string on the right is reversed
# - we could use .casefold() to ignore case
# - 
# - if these strings match return True
# - else return False

# C

import re

def is_real_palindrome(string):
    string = re.sub(r'[^A-Za-z0-9\s]', '', string.casefold())
    string = string.replace(" ", "")

    if len(string) % 2 == 0:
        half = len(string) // 2
        left_half = string[:half]
        right_half = string[half:]
        reverse_right = right_half[::-1]
        
        return (left_half == reverse_right)

    if len(string) % 2 == 1:
        half = len(string) // 2
        left_half = string[:half]
        right_half = string[half + 1:]
        reverse_right = right_half[::-1]

        return (left_half == reverse_right)
    
print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam")== True) # True