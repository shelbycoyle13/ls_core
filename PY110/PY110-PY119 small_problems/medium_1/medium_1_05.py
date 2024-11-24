# Write a function that takes a string as an argument and returns that string with every occurrence of a "number word" -- 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' -- converted to its corresponding digit character.

# You may assume that the string does not contain any punctuation.

# message = 'Please call me at five five five one two three four'
# print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# # Should print True

'''
P
- input = string
- output = new string with digit words converted to numbers
- explicit = string has no punctuation

E
# message = 'Please call me at one two three four five'
# print(word_to_digit(message) == "Please call me at 1 2 3 4 5")

D
dictionary
list

A
- create a dictionary with number words as keys and digits as values
    - ex: "one": 1
- to split string by whitespace (turns into a list)
- go through list word by word
    - if the word is a key in the dictionary:
        - replace the word at that index with the dictionary value for that key
    - if the word is NOT in the dictionary:
        - append the word in a new string
- return new string

C
'''
numeric_words = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
    "zero" : 0
}
def word_to_digit(string):
    final_string = ""
    list_of_words = string.split()

    for word in list_of_words:
        if word in numeric_words:
            final_string += str(numeric_words[word]) + " "
        else:
            final_string += word + " "
    return final_string[:-1]
        
message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")

message = 'Please call me at one two three four five'
print(word_to_digit(message) == "Please call me at 1 2 3 4 5")