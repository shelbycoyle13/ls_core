# Palindromic Strings (Part 1)

# Write a function that returns True if the string passed as an argument is a palindrome, False otherwise. A palindrome reads the same forwards and backwards. For this problem, the case matters and all characters matter.

# All of these examples should print True

# print(is_palindrome('madam') == True)
# print(is_palindrome('356653') == True)
# print(is_palindrome('356635') == False)

# # case matters
# print(is_palindrome('Madam') == False)

# # all characters matter
# print(is_palindrome("madam i'm adam") == False)

# P 
# input = string
# output = Boolean
# explicit = We're passing in a string that can be any length, with any cases, and any characters. Case and characters matter.
# implicit = It doesn't appear we can have empty strings.

# E
# Examples / test cases are above

# D
# For loops, strings

# A
# - After receiving the string, we should split the string in half
# - if the length of the string is odd, include a halfway point
# - compare the string on the "left" with the string on the "right" but the string on the right is reversed
# - if these strings match return True
# - else return False

# C

def is_palindrome(string):
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

# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)

#Second, way more concise answer - slicing is a lifesaver!
def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False