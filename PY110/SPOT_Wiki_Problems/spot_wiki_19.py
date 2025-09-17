# 19. Title-ize
# A string is considered to be in title case if each word in the string is either:
# a) Capitalized (that is, only the first letter of the word is in upper case)
# b) Considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalized.

# Write a function that will convert a string into title case, given an optional list of exceptions (minor words). The list of minor words will be given as a string with each word separated by a space. Your function should ignore the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.

# Examples:
# title_case('a clash of KINGS', 'a an the of') # should return 'A Clash of Kings'
# title_case('THE WIND IN THE WILLOWS', 'The In') # should return 'The Wind in the Willows'
# title_case('the quick brown fox') # should return 'The Quick Brown Fox'

"""
P
input = two strings
output = one string
explicit = convert the string argument to title case. the first word of the string is always capitalized. other non-exception words are also capitalized
implicit = 

E

D
strings
list

A
-initialize a new empty string
-split string by words, initialize to a list variable
-for i, word in enumerate(list)
    -if word in 2nd string and i != 0:
        - final sring += word
    -else 
        -final string += word.title()

return final string

C
"""

def title_case(string, exceptions=None):
    final_string = ""

    list_of_words = string.lower().split()


    for i, word in enumerate(list_of_words):
        if exceptions is None:
            final_string += word.title() + " "
        elif word in exceptions.lower() and i != 0:
            final_string += word.lower() + " "
        else:
            final_string += word.title() + " "
    
    return final_string[:-1]

print(title_case('a clash of KINGS', 'a an the of') == 'A Clash of Kings') # should return 'A Clash of Kings'
print(title_case('THE WIND IN THE WILLOWS', 'The In') == 'The Wind in the Willows') # should return 'The Wind in the Willows'
print(title_case('the quick brown fox') == 'The Quick Brown Fox') # should return 'The Quick Brown Fox'