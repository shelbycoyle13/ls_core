# 31. Highest Scoring Word

# # Find the highest scoring word in a string.
# # Each letter scores points based on its position in the alphabet: a = 1, b = 2, c = 3, ... z = 26.
# # Return the highest scoring word. If two words score the same, return the word that appears earliest in the string.

#high('man i need a taxi up to ubud') == 'taxi'
#high('what time are we climbing up the volcano') == 'volcano'
#high('take me to semynak') == 'semynak'
#high('aaa b') == 'aaa'

"""
P
input = a string
output = one word from the string
explicit = we want to return the word that has the highest score. each letter is worth its place in the alphabet.
implicit = looks like all strings are in lowercase. some words are not real english words.

E

D
string
dict

A
initialize a dict, key = letter, value = position in alphabet

split the string into words
highest_word_total = 0
highest_word = None

iterate through the list of words, for word in list
    word_point_total = 0
    for letter in word
        word_points_total += dict[letter]
    if word_point_total > highest_word_total
        highest_word_total = word_point_total
        highest_word = word
    
    return word


C
"""
def high(string):

    alphabet = {
        "a" : 1,
        "b" : 2,
        "c" : 3,
        "d" : 4,
        "e" : 5,
        "f" : 6,
        "g" : 7,
        "h" : 8,
        "i" : 9,
        "j" : 10,
        "k" : 11,
        "l" : 12,
        "m" : 13,
        "n" : 14,
        "o" : 15,
        "p" : 16,
        "q" : 17,
        "r" : 18,
        "s" : 19,
        "t" : 20,
        "u" : 21,
        "v" : 22,
        "w" : 23,
        "x" : 24,
        "y" : 25,
        "z" : 26
    }

    list_of_words = string.split()

    highest_word_total = 0
    highest_word = list_of_words[0]

    for word in list_of_words:
        word_point_total = 0
        for letter in word:
            word_point_total += alphabet[letter]
        if word_point_total > highest_word_total:
            highest_word_total = word_point_total
            highest_word = word
    
    return highest_word

print(high('man i need a taxi up to ubud') == 'taxi')
print(high('what time are we climbing up the volcano') == 'volcano')
print(high('take me to semynak') == 'semynak')
print(high('aaa b') == 'aaa')