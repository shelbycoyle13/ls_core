#  Count the letters in a string

#  Write a function that takes a string as input and counts the occurrences of each
# lowercase letter in the string. Return the counts in a dictionary where the
# letters are keys and their counts are values.

# letter_count('launchschool') #=> { 'a': 1, ‘c’: 2, ‘h’: 2, ‘l’: 2, ‘o’: 2, ‘u’: 1 } 

### The solution above should be corrected, missing letters n and s!!!

"""
P
input = string
output = dictionary
explicit = letters are keys, counts are the values. we're only counting the lowercase letters
implicit = we could assume no empty strings?

E
# letter_count('cookie') #=> {"c": 1, "o": 2, "k": 1, "i": 1, "e": 1}

D
strings
dictionaries

A
-initialize empty dictionary
-iterate though each character of the string
    -if a char is lowercase
        - add to dictionary and add 1 to the value
    -else
        -continue
-return dictionary

C
"""

def letter_count(string):
    letter_dict = {}

    for char in string:
        if char.islower() and char not in letter_dict:
            letter_dict[char] = 1
        elif char.islower() and char in letter_dict:
            letter_dict[char] += 1

    return letter_dict

# print(letter_count("launchschool")) # {'l': 2, 'a': 1, 'u': 1, 'n': 1, 'c': 2, 'h': 2, 's': 1, 'o': 2}
print(letter_count('cookie') == {"c": 1, "o": 2, "k": 1, "i": 1, "e": 1})