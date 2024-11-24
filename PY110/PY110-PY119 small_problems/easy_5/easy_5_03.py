# Write a function that takes a list of strings and returns a list of the same string values, but with all vowels (a, e, i, o, u) removed.

# # All of these examples should print True
# original = ['abcdefghijklmnopqrstuvwxyz']
# expected = ['bcdfghjklmnpqrstvwxyz']
# print(remove_vowels(original) == expected)        # True

# original = ['green', 'YELLOW', 'black', 'white']
# expected = ['grn', 'YLLW', 'blck', 'wht']
# print(remove_vowels(original) == expected)        # True

# original = ['ABC', 'AEIOU', 'XYZ']
# expected = ['BC', '', 'XYZ']
# print(remove_vowels(original) == expected)        # True

"""
P
input = a list of string(s)
output = a list of string(s) with the vowels removed
explicit = a, e, i, o, u is removed
implicit = the returning string could possibly be an empty string

E
# original = ['what', 'is', 'up']
# expected = ['wht', 's', 'p']
# print(remove_vowels(original) == expected)        # True

D
list
strings

A
-we should set a list of just the vowels
-create an empty list
-iterate through the strings, for every string in strings
-create an empty string
    -for every char in string
        -if char not in vowels list
            -add to the new string
        -add string to the new list
-return the new list

C
"""
VOWELS = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

def remove_vowels(lst):

    new_list = []

    for string in lst:
        new_string = ""
        for char in string:
            if char not in VOWELS:
                new_string += char
        new_list.append(new_string)
    
    return new_list

    # return [strip_vowels(string) for string in lst]

# def strip_vowels(string):
#     no_vowels = [char
#             for char in string
#             if char not in VOWELS]

#     return "".join(no_vowels)

original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True

original = ['what', 'is', 'up']
expected = ['wht', 's', 'p']
print(remove_vowels(original) == expected)        # True