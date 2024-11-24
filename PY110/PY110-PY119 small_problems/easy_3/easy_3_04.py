# Write a function that takes a string, doubles every consonant in the string, and returns the result as a new string. The function should not double vowels ('a','e','i','o','u'), digits, punctuation, or whitespace.

# You may assume that only ASCII characters will be included in the argument.

# # All of these examples should print True
# print(double_consonants('String') == "SSttrrinngg")
# print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
# print(double_consonants('July 4th') == "JJullyy 4tthh")
# print(double_consonants('') == "")

"""
P
input = string
output = string
explicit = double consonants only
implicit = if a string is empty, return an empty string

E
# print(double_consonants('Wassup') == "WWassssupp") #True

D
loop

A
-initialize an empty final string
-for every char in the string:
    - if char is alphabetical AND not a vowel:
    - double that character and concatenate to the empty string
-return the final string

C
"""

def double_consonants(string):
    final_string = ""
    for char in string:
        if char in ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]:
            final_string += char
        elif char.isalpha():
            final_string += char * 2
        else:
            final_string += char
    return final_string

print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")