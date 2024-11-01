# Letter Swap
# Given a string of words separated by spaces, write a function that swaps the first and last letters of every word.

# You may assume that every word contains at least one letter, and that the string will always contain at least one word. You may also assume that each string contains nothing but words and spaces, and that there are no leading, trailing, or repeated spaces.

# print(swap('Oh what a wonderful day it is')
#       == "hO thaw a londerfuw yad ti si")  # True
# print(swap('Abcde') == "ebcdA")            # True
# print(swap('a') == "a")                    # True

# P 
# input = a string (of words, separated by single spaces)
# output = a string (with the first and last letter of each word swapped)
# explicit = every word has at least one letter. a string will always have at least one word. there are only alphabetic characters and single whitespace. no leading or trailing whitespace.
# implicit = we are swapping exact characters, regardless of case.

# E
# Examples / test cases are above

# D
# Strings, lists

# A
# - First we take the string; we should split the string into substrings
# - We should iterate through the characters of the substring
# - Create a new string
# - Create a new substring
# - Assign the last character to the first index of the new substring
# - Assign the first character to the last index of the new substring
# - Add these characters to the new substring
# - Add the new substrings to the new string
# - Return the new string

# C
def swap(string):
    words = string.split()
    
    new_string = ""
    new_word = ""

    for word in words:

        if len(word) == 1:
            new_word += word
            space = " "
            new_word += space
    
        else:
            first_letter = word[-1]
            new_word += first_letter

            middle = word[1:-1]
            new_word += middle

            last_letter = word[0]
            new_word += last_letter

            space = " "
            new_word += space

    new_string += new_word.strip()

    return new_string

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
