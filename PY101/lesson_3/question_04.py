# Using the following string, print a string that contains the same value, but using all lowercase letters except for the first character, which should be capitalized.

munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'

def sentence(string):
    new_sentence = string.capitalize()
    return new_sentence

print(sentence(munsters_description))