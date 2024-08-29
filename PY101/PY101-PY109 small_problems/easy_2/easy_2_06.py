# Write a function that returns the next to last word in the string argument.
# Words are any sequence of non-blank characters.
# You may assume that the input string will always contain at least two words.

def penultimate(string):
    list_of_words = string.split()
    return list_of_words[-2]

# These examples should print True
# print(penultimate("last word") == "last")
# print(penultimate("Launch School is great!") == "is")

# Further Exploration
# Our solution ignored two edge cases since we explicitly stated that you didn't have to handle them: strings that contain no words or just one word.

# Suppose we need a function that retrieves the middle word of a phrase/sentence. What edge cases need to be considered? How would you handle those edge cases without ignoring them? Write a function that returns the middle word of a phrase or sentence. It should handle all of the edge cases you thought of.

def middle_word(phrase):
    list_of_words = phrase.split()

    if phrase == "":
        return "This phrase is totally empty."
    elif len(list_of_words) == 1:
        return "This phrase only has 1 word."
    elif len(list_of_words) % 2 == 0:
        half = len(list_of_words) // 2
        middle_index_word = list_of_words[half - 1]
        return middle_index_word
    else:
        half = len(list_of_words) // 2
        middle_index_word = list_of_words[half]
        return middle_index_word
    
print(middle_word("This should grab the middle word now"))