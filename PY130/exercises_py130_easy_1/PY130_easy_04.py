# Lengths of Strings
# Use map to create a list of lengths of each string in the original list.

words = ["hello", "how", "are", "you"]

words_length_list = list(map(lambda word: len(word), words))

print(words_length_list)

#LS Solution:
# lengths = list(map(len, ["apple", "banana", "cherry"]))