# Problem 8

# Create a function that takes a non-empty string as an argument. The string consists entirely of lowercase alphabetic characters. The function should return the length of the longest vowel substring. The vowels of interest are "a", "e", "i", "o", and "u".

# The below tests should each print True.

"""
P
input = a string
output = an integer (the length of the longest vowel substring)
explicit = we want to return the length of the longest vowel substring only
implicit = 

E

D
-strings

A
-high level:
    1) get the substrings
    2) get the substrings that consist of only vowels
    3) get the longest substring from only vowels
    4 return the length of that substring

-initialize a list of just the vowels
-initialize empty list to hold substrings with only vowels

-for i in range(len(string))
    -for j in range(1, len(string) + 1)
        -if [i:j] in vowels
            -add to empty substring vowel list

-return len(max(substring vowel list))

C
"""
def longest_vowel_substring(string):
    vowels = ["a", "e", "i", "o", "u"]
    substrings = []
    just_vowel_substrings = []
    
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            substrings.append(substring) # Good to append substrings to a list

            if all(char in vowels for char in substring): # This is saying "Check if everything inside the () is True. For every character in the substring, is every character a vowel?"
                just_vowel_substrings.append(substring) # If True, add to the just_vowels_substrings list
            
    if not just_vowel_substrings: # If this list is empty, return 0
        return 0
    
    return len(max(just_vowel_substrings, key=len)) # Remember, we can't use max with strings, it just returns the later ones in the alphabet, we have to use the key parameter and return the substring that has the longest length. Then, we return the actual length.

    

print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)

#Second, more recent answer, which I like better:

def longest_vowel_substring(string):
    vowels = "aeiou"
    current_substring = ""
    longest_substring = ""
    
    for char in string:
        if char in vowels:
            current_substring += char
            if len(current_substring) > len(longest_substring): #If the length of the current substring is greater than the longest
                longest_substring = current_substring #The new longest substring is now equal to the new current
        else:
            current_substring = ""

    return len(longest_substring)