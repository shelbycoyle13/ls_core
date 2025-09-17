# Longest Chain of Vowels

# Write a function that takes a lowercase string as input and returns the length of the longest substring that consists entirely of vowels (a, e, i, o, u).

# Examples:
# solve("roadwarriors") # should return 2
# solve("suoidea") # should return 3

"""
P
input = a lowercase string
output = an integer (that represents the length of the longest vowel substring)
explicit = sustring is made entirely of vowels, function accepts lowercase string
implicit = 

E
# solve("wassuupp") # should return 2

D
strings
list

A
-create a list dedicated to holding the vowels
-initialize a current length variable
-initialize a max length variable
-iterate through the characters of the string
    -if char is a vowel
        - add +1 to the current length
    else
        -if current length > max length
            max length = current length
        -current length = 0
    return max length
C
"""
vowels = ["a", "e", "i", "o", "u"]

def solve(string):
    current_length = 0
    max_length = 0

    for char in string:
        if char in vowels:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 0

    return max_length

print(solve("roadwarriors")) # should return 2
print(solve("suoidea")) # should return 3
print(solve("wassuupp")) # should return 2)