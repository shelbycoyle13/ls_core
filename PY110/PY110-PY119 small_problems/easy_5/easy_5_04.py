# Write a function that takes a string as an argument and returns a list that contains every word from the string, with each word followed by a space and the word's length. If the argument is an empty string or if no argument is passed, the function should return an empty list.

# You may assume that every pair of words in the string will be separated by a single space.

# # All of these examples should print True
# words = 'cow sheep chicken'
# expected_result = ['cow 3', 'sheep 5', 'chicken 7']
# print(word_lengths(words) == expected_result)        # True

# words = 'baseball hot dogs and apple pie'
# expected_result = ['baseball 8', 'hot 3', 'dogs 4',
#                    'and 3', 'apple 5', 'pie 3']
# print(word_lengths(words) == expected_result)        # True

# words = "It ain't easy, is it?"
# expected_result = ['It 2', "ain't 5", 'easy, 5',
#                    'is 2', 'it? 3']
# print(word_lengths(words) == expected_result)        # True

# big_word = 'Supercalifragilisticexpialidocious'
# print(word_lengths(big_word) == [f'{big_word} 34'])  # True

# print(word_lengths('') == [])                        # True
# print(word_lengths() == [])                          # True

"""
P
input = a string
output = a list of strings
explicit = we want each element in the list to feature the word and its length. an empty string or empty argument returns an empty list
implicit = in this scenario, words are separated by spaces and even include symbols as part of their length

E
# words = 'pasta tacos and pizza'
# expected_result = ['pasta 5', 'tacos 5', 'and 3', 'pizza 5']
# print(word_lengths(words) == expected_result)        # True

D
lists
strings

A
-split the string (by whitespace)
-create a new empty list
-in the new list with the words, iterate for each word in list
    -create an empty string
    -add the word to the empty string
    -add a space and the length of the word to the empty string
-return the new list

C
"""
def word_lengths(string=""):
    words = string.split()

    final_list = []
    for word in words:
        final_string = ''
        final_string += word + ' ' + str(len(word))
        final_list.append(final_string)
    return final_list

    # return [f"{word} {len(word)}" for word in words]


words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True