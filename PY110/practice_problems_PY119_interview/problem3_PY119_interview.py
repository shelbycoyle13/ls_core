# Create a function that takes a string argument and returns a copy of the string with every second character in every third word converted to uppercase. Other characters should remain the same.

# The below tests should each print True.

"""
P
input = a string
output = a new string
explicit = every third word's second character should be uppercase
implicit = 

E

D
strings

A
-initialize a final empty string
--for i, char in enumerate(string)
        -if i == 2:
            final_string += char.upper()
        -else
            final_string += char
C
"""
def to_weird_case(string):
    final_string = ""

    for i, word in enumerate(string.split()):
        final_word = "" #Best to break up into adding one word at a time
        if (i + 1) % 3 == 0:
            for i2, char in enumerate(word):
                if i2 % 2 == 1: #Keep the different indexes with separate variables
                    final_word += char.upper()
                else:
                    final_word += char
        else:
            final_word = word

        final_string += final_word + " "

    return final_string.strip() #Strips away any extra whitespace on either side


original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original)  == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)

# Second, more recent answer (similar to above, slight differences)
def to_weird_case(string):
    final_word = ""
    list_words = string.split()
    for i, word in enumerate(list_words):
        if (i + 1) % 3 == 0:
            for i, char in enumerate(word):
                if (i + 1) % 2 == 0:
                    final_word += char.upper()
                else:
                    final_word += char
            final_word += " "
        else:
            final_word += word + " "

    return final_word[:-1]