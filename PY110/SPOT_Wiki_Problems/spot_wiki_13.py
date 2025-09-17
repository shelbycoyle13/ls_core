# 13. Kebabize a String
# Modify the kebabize function so that it converts a camel case string into a
# kebab case. Kebab case separates words with dashes '-'; camel case identifies
# separate words by upcasing the first character in each new word.

# Examples:
# kebabize('camelsHaveThreeHumps') # should return 'camels-have-three-humps'
# kebabize('myCamelHas3Humps') # should return 'my-camel-has-humps'

"""
P
input = a string
output = a string
explicit = we want to separate each word with a hyphen. words are defined by the camel case
implicit = digits must not be considered a word based on the second test case

E

D
strings

A
-intialize new string
-iterate through the string, for char in string
    -if not char.isalpha
        -continue
    -elif char is uppercase
        - new_string += "-"char.lower
    else:
        - new_string += char

-return final string

C
"""

def kebabize(string):
    final_string = ""

    for char in string:
        if not char.isalpha():
            continue
        elif char.isupper():
            final_string += "-"+ char.lower()
        else:
            final_string += char

    return final_string

print(kebabize('camelsHaveThreeHumps')) # should return 'camels-have-three-humps'
print(kebabize('myCamelHas3Humps')) # should return 'my-camel-has-humps'