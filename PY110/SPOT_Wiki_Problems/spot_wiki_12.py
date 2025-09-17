# 12. Detect the Pangram
# A pangram is a sentence that contains every single letter of the alphabet at
# least once. Given a string, detect whether or not it is a pangram.
# Return True if it is, False if not. Ignore numbers and punctuation.

# Examples:
# pangram("The quick brown fox jumps over the lazy dog.") # should return True
# pangram("This is not a pangram.") # should return False

"""
P
input = a string
output = a Boolean
explicit = if the string has each letter at least once, return True; False otherwise. ignore numbers and punctuation
implicit = 

E

D
strings

A
-initialize an alphabet string
-iterate through the string argument
    -if not char.isalpha
        -continue
    -elif letter in alphabet is not in string argument
        -return False
    -else, return True

C
"""

def pangram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in alphabet:
        if letter not in string:
            return False
    
    return True

print(pangram("The quick brown fox jumps over the lazy dog.")) # should return True
print(pangram("This is not a pangram.")) # should return False