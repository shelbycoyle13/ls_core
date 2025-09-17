# Letter Counter (Part 1)

# Write a function that takes a string consisting of zero or more space-separated words and returns a dictionary that shows the number of words of different sizes.

# Words consist of any sequence of non-space characters.

# All of these examples should print True

# string = 'Four score and seven.'
# print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

# string = 'Hey diddle diddle, the cat and the fiddle!'
# print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

# string = 'Humpty Dumpty sat on a wall'
# print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

# string = "What's up doc?"
# print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

# print(word_sizes('') == {})

# P 
# input = string
# output = dictionary (keys are the length of the word, values are the occurences of that length)
# explicit = strings can be empty. words include non-space characters.
# implicit = 

# E
# Examples / test cases are above

# D
# Lists and dictionaries

# A
# - We take the string and split it using whitespace as a separator.
# - These substrings would go into a list.
# - We can iterate through the list and count the length of each substring.
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
        my_key = len(substring)
        word_length_count[my_key] = word_length_count.get(my_key, 0) + 1

    return word_length_count

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})

#Second, more readable answer:

def word_sizes(string):

    if not string:
        return {}
    
    list_of_words = string.split()

    word_length_dict = {}

    for word in list_of_words:
        if len(word) not in word_length_dict:
            word_length_dict[len(word)] = 1
        else:
            word_length_dict[len(word)] += 1

    return word_length_dict