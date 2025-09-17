# 38. Update string
# Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd" . Your task is to process a string with "#" symbols and return the final state of the string.

#print(clean_string('abc#d##c') == "ac")
#print(clean_string('abc####d##c#') == "")

"""
P
input = a string
output = a string
explicit = we want to return the final state of the string. Essentially, any letter that comes before a # gets removed; it acts like a backspace
implicit = empty strings are possible as a final result

E

D
strings

A
initialize empty final string
iterate through the strings, for char in string
    if char == #
        replace char before it with ""
    else
        add char to final string
        
return final string

"""
def clean_string(string):
    characters_list = []

    for i, char in enumerate(string):
        if char == "#" and characters_list:
            characters_list.pop()
        else:
            characters_list += char
    
    return "".join(characters_list)

print(clean_string('abc#d##c') == "ac")
print(clean_string('abc####d##c#') == "")