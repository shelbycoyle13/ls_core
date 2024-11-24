# Write a function that takes a string, doubles every character in the string, then returns the result as a new string.

# print(repeater('Hello') == "HHeelllloo")              # True
# print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
# print(repeater('') == "")                             # True

"""
P
input = string
output = string
explicit = we are taking every character an returning two of them, including any symbols
implicit = if it's an empty string, we're returning an empty string

E
print(repeater("Wasup") == "WWaassuupp") #True

D
loops

A
- let's start with an empty final string
- we should iterate through the current string, start with the first character, multiply by 2, and concatenate those two character to the empty string
- move on to the next character, same action...to the end of the string
- return final string

C
"""

def repeater(string):
    final_string = ""
    for char in string:
        final_string += char * 2
    return final_string

    # return "".join([char * 2 for char in string]) #Practicing with a list comprehension, then joining these elements into a string

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True
print(repeater("Wasup") == "WWaassuupp") #True