# 32. Replace Char with Score
# # Given a string, replace every letter with its position in the alphabet.
# # If anything in the text isn't a letter, ignore it and don't return it.

# p alphabet_position("The sunset sets at twelve o' clock.") == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
# p alphabet_position("-.-'") == ""

"""
P
input = a string
output = a string (of integers)
explicit = replace every letter with its numerical position in the alphabet. if its not a letter, ignore it and dont return anything in its place
implicit = case is irrelevant. when we replace each letter with an integer we put a space in between each integer in one long string. if the entire string is non-alphabetical, return an empty string.

E

D
strings
dict

A
initialize an alphabet string, alphabet = abcdefghijklmnopqrstuvwxyz

initialize empty final string 

iterate through the string (lowercase), for letter in string
    if the letter is in the alphabet
        final_string += index + 1

return final string

C
"""
def alphabet_position(string):
    alphabet = "abcdefghijklmnopqrstuvwxy"

    final_string = ""

    for letter in string.lower():
        if letter in alphabet:
            final_string += str(alphabet.index(letter) + 1) + " "

    return final_string[:-1]

print(alphabet_position("The sunset sets at twelve o' clock.") == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
print(alphabet_position("-.-'") == "")