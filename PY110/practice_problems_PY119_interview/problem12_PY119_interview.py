# Create a function that takes a string as an argument and returns True if the string is a pangram, False if it is not.

# Pangrams are sentences that contain every letter of the alphabet at least once. For example, the sentence "Five quacking zephyrs jolt my wax bed." is a pangram since it uses every letter at least once. Note that case is irrelevant.

# The below tests should each print True.

# print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
# print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
# print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
# print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
# print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

# my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
# print(is_pangram(my_str) == True)

"""
P
input = a string
output = a Boolean
explicit = if a string is a pangram, return True. Case is irrelevant. A pangram is when a sentence has at least every letter in the alphabet one time.
implicit = 

E


D
strings

A
-initialize a string that has each character in the alphabet just once, call it alphabet
-iterate through the alphabet, for letter in alphabet
    -if letter is not in string (using casefold, since case is irrelevant)
        -return False
    
    -return True

C
"""

def is_pangram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in alphabet:
        if letter not in string.casefold():
            return False
    return True
        
print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)