# Letter Counter (Part 2)
# Modify the word_sizes function from the previous exercise to exclude non-letters when determining word size. For instance, the word size of "it's" is 3, not 4.

# All of these examples should print True

# string = 'Four score and seven.'e
# print(word_sizs(string) == {4: 1, 5: 2, 3: 1})

# string = 'Hey diddle diddle, the cat and the fiddle!'
# print(word_sizes(string) == {3: 5, 6: 3})

# string = 'Humpty Dumpty sat on a w@ll'
# print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

# string = "What's up doc?"
# print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

# print(word_sizes('') == {})

# P 
# input = string
# output = dictionary (keys are the length of the word, values are the occurences of that length)
# explicit = strings can be empty. words must be all alphabetic characters.
# implicit = 

# E
# Examples / test cases are above

# D
# Lists and dictionaries

# A
# - We take the string and split it using whitespace as a separator.
# - These substrings would go into a list.
# - We can iterate through the list and count the alphabetic characters of each substring.
# - Set the length as a key for the dictionary.
# - Set the current count to 0 for each length.
# - Add 1 to the count for each occurence of that length.
# - Add the count as the value of the key.
# - Return the dictionary

# C
def word_sizes(string1):
    word_length_count = {}

    substrings = string1.split()
    
    for substring in substrings:
        my_key = 0
        for character in substring:
            if character.isalpha():
                my_key += 1
            else:
                continue
        word_length_count[my_key] = word_length_count.get(my_key, 0) + 1
    return word_length_count

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})