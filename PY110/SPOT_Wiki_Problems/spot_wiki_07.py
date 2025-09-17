# The Nth Char
# Write a function that takes a list of words and constructs a new word by concatenating the nth letter from each word, where n is the position of the word in the list.

# Example:
# nth_char(['yoda', 'best', 'has']) # should return 'yes'

"""
P
input = a list (of strings)
output = one string
explicit = the new word is built through each position of the words in the list
implicit = 

E

D
list
strings

A
-new word = ""
-for each word in list
    -for each letter in word
        -if index of letter = index of word in list + 1
            += letter to new word
-return new word

C
"""

def nth_char(lst):
    new_word = ""

    for i, word in enumerate(lst):
        new_word += word[i]

    return new_word

print(nth_char(['yoda', 'best', 'has'])) # should return 'yes'