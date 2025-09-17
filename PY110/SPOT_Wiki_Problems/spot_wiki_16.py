# 16. Spin Words
# Write a function that takes in a string of one or more words and returns the same string, but with all words of five or more letters reversed. Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# Examples:
# spin_words("Hey fellow warriors") # should return "Hey wollef sroirraw"
# spin_words("This is a test") # should return "This is a test"
# spin_words("This is another test") # should return "This is rehtona test"

"""
P
input = a string
output = a string
explicit = all words in the new string that have a length of 5+ need to be reversed.
implicit = 

E

D
strings

A
-initialize a list assigned to string.split()
-initialize an empty string
-for word in list
    -if len(word) >= 5
        -empty string += reversed(word) + " "
    else:
        -empty string += word + " "

-return final string[:-1]

C
"""
def spin_words(string):
    list_of_words = string.split()

    final_string = ""

    for word in list_of_words:
        if len(word) >= 5:
            final_string += word[::-1] + " "
        else:
            final_string += word + " "

    return final_string[:-1]


print(spin_words("Hey fellow warriors") == "Hey wollef sroirraw") # should return "Hey wollef sroirraw"
print(spin_words("This is a test") == "This is a test") # should return "This is a test"
print(spin_words("This is another test") =="This is rehtona test" ) # should return "This is rehtona test"