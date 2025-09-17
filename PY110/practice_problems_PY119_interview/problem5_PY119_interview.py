# Problem 5
# Create a function that takes a string argument and returns the character that occurs most often in the string. If there are multiple characters with the same greatest frequency, return the one that appears first in the string. When counting characters, consider uppercase and lowercase versions to be the same.
# The below tests should each print True.

"""
P
input = a string
output = a single character that occurs most often. if there's a tie, return the one that appears first
explicit = upper and lowercase versions of a character should count the same
implicit =

E
print(most_common_char('Appa') == 'a')

D
strings
dictionary

A
initialize an empty dictionary
-for char in string.lower():
    -if char not in dict
        -add char : 1
    - else
        char += 1

return max in dict
    
C
"""

def most_common_char(string):
    letter_dict = {}

    for char in string.lower():
        if char not in letter_dict:
            letter_dict[char] = 1
        else:
            letter_dict[char] += 1
    
    return max(letter_dict, key=letter_dict.get) # We can use the max() function on a dictionary, but we have to specify the key parameter. The key needs to be dict.get to get all of the values from the dictionary. If we leave it as max(dict), it returns the largest key, in this case it would return the last letter in the alphabet.

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')

#Second, more recent answer, possibly easier to remember

def most_common_char(string):
    letters_dict = {}
    for char in string.casefold():
        if char not in letters_dict:
            letters_dict[char] = 1
        else:
            letters_dict[char] += 1

    max_freq = max(letters_dict.values()) # We've figured out the highest value in the dict is 4

    for char in string.casefold(): # Iterate over the string one more time
        if letters_dict[char] == max_freq: #If any of the chars in the string match the highest value
            return char #Just return that first char
        

#Third, more recent answer, proably the easiest to remember since the implemenation is basic, no use of max()

def most_common_char(string):
    dict_of_chars = {} #Empty dictionary initialization

    for char in string.lower(): #Iterating through the string, lowercase
        if char not in dict_of_chars:
            dict_of_chars[char] = 1
        else:
            dict_of_chars[char] += 1 #Now we have the dictionary with the chars and values

    top_occurrence_amount = 0 #Setting an initial amount to "beat"
    top_occurrence_char = "" #Setting an initial char, empty since we don't want to make any other assumptions as to what the char "should" be

    for key, value in dict_of_chars.items(): #We're iterating through the dictionary
        if value > top_occurrence_amount: #If a value in the dictionary is greater than the top one
            top_occurrence_amount = value #The new top value is the same as the current value
            top_occurrence_char = key #And the char "most occurred" is the same as the current key
    
    return top_occurrence_char #After the loop is finished, return that most occurred character