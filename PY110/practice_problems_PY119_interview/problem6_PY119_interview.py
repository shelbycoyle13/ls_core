# Problem 6
# Create a function that takes a string argument and returns a dict object in which the keys represent the lowercase letters in the string, and the values represent how often the corresponding letter occurs in the string.
# The above tests should each print True.

"""
P
input = a string
output = a dictionary
explicit = keys  = lowercase letters in the string, values = occurrences
implicit = we're only counting lowercase letters, no other types of characters!

E

D
strings
dictionaries

A
-initialize empty dict
-iterate through the string, for char in string
    -if char.lower() not in dict:
        -dict[char] = 1
    else:
        -dict[char] += 1
-return dict


C
"""
def count_letters(string):
    letters_dict = {}

    for char in string:
        if char.isalpha():
            if char.islower():
                if char not in letters_dict:
                    letters_dict[char] = 1
                elif char in letters_dict:
                    letters_dict[char] += 1

    return letters_dict


expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})

#Second, more recent answer. Similar:
def count_letters(string):
    final_dict = {}

    for char in string:
        if char.islower(): #.islower ignores non-alpha characters
            if char not in final_dict:
                final_dict[char] = 1
            else:
                final_dict[char] += 1
        else:
            continue

    return final_dict

#Third, more recent answer. Also similar, except forgot that .islower only deals with alphabetical characters anyway:

def count_letters(string):

    final_dict = {}

    for char in string:
        if char.isalpha() and char.islower():
            if char not in final_dict:
                final_dict[char] = 1
            else:
                final_dict[char] += 1
        else:
            continue
    
    return final_dict

#Fourth time, way more succinct

def count_letters(string):

    final_dict = {letter : string.count(letter) for letter in string if letter.islower()}

    return final_dict