# Starting with the string:

munsters_description = "The Munsters are creepy and spooky."

# print the string with the case of all letters swapped:

# "tHE mUNSTERS ARE CREEPY AND SPOOKY."

# That is, lowercase letters are converted to uppercase, and uppercase letters are converted to lowercase"

def change_case(string):
    new_string = ""
    for char in string:
        if char.islower():
            new_string += char.upper()
        elif char.isupper():
            new_string += char.lower()
        elif char.isspace():
            new_string += ' '
    return new_string

print(change_case(munsters_description))