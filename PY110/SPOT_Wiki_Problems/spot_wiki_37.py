# 37. Encode Duplicates
# # The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

#print(duplicate_encode("din") == "(((")
#print(duplicate_encode("recede") == "()()()")
#print(duplicate_encode("Success") == ")())())")
#print(duplicate_encode("(( @") == "))((")

"""
P
input = a string
output = a string
explicit = for every letter in the string we want to convert characters that only appear once to ( and duplicates to )
implicit = case is irrelevant. it looks like non-alphabetic characters and whitespace also count towards converting to ()

E

D
strings

A
initialize a new empty final string
iterate over the string in its lowercase form, for char in string
    if char count is greater than 1
        add )
    else
        add (

return final string

C
"""
def duplicate_encode(string):
    final_string = ""

    for char in string.lower():
        if string.count(char) > 1:
            final_string += ")"
        else:
            final_string += "("

    return final_string

print(duplicate_encode("din") == "(((")
print(duplicate_encode("recede") == "()()()")
print(duplicate_encode("Success") == ")())())")
print(duplicate_encode("(( @") == "))((")