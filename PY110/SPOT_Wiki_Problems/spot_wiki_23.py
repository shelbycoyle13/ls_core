# 23. Longest alphabetical substring
# Write a function `longest(s)` that finds and returns the longest substring of
# `s` where the characters are in alphabetical order.

# Example:
# longest('asd')                  # should return 'as'
# longest('nab')                  # should return 'ab'
# longest('abcdeapbcdef')         # should return 'abcde'
# longest('asdfaaaabbbbcttavvfffffdf') # should return 'aaaabbbbctt'
# longest('asdfbyfgiklag')        # should return 'fgikl'
# longest('z')                    # should return 'z'
# longest('zyba')                 # should return 'z'

"""
P
input = a string
output = a string
explicit = we want to return the longest substring that is in alphabetical (ascending) order
implicit = 

E

D
strings

A
-longest_string = ""
-current_string = ""

-for i, letter in enumerate(substring)
    -if ord(letter) > ord(substring[i-1]))
        - current_string += letter
        - if current_string > longest_string
            -longest string = current_string
    -else
        current_string = ""

-return longest string

C
"""

def longest(string):
    longest_string = ""
    current_string = string[0] #Start the string with the first character

    for i in range(1, len(string)): #We want to focus on the indexes here
        if ord(string[i]) >= ord(string[i-1]):
            current_string += string[i] #Same as saying "The current letter"
        else: 
            if len(current_string) > len(longest_string): #Before resetting, compare the two strings
                longest_string = current_string
            current_string = string[i] #If the sequence breaks, don't reset it to empty, reset to the current character

    if len(current_string) > len(longest_string): #We have to compare the two strings one final time. Why? Because the final current_string is the longest out of them all
                longest_string = current_string

    return longest_string


###Second, more recent answer, less complicated now to understand and code, less error prone:

def longest(string):

    substrings = [string[i:j] for i in range(len(string))
                    for j in range(i + 1, len(string) + 1)]
  
    sorted_substrings = [substring for substring in substrings if list(substring) == sorted(substring)]

    sorted_substrings.sort(key=lambda substring: len(substring), reverse=True)

    return sorted_substrings[0]

print(longest('asd') == "as")                  # should return 'as'
print(longest('nab') == "ab")                  # should return 'ab'
print(longest('abcdeapbcdef') == "abcde")        # should return 'abcde'
print(longest('asdfaaaabbbbcttavvfffffdf') == "aaaabbbbctt") # should return 'aaaabbbbctt'
print(longest('asdfbyfgiklag') == "fgikl")        # should return 'fgikl'
print(longest('z') == "z")                    # should return 'z'
print(longest('zyba') == "z")                 # should return 'z'

###Third time

# def longest(string):
    
#     substrings = [string[i:j] for i in range(len(string))
#         for j in range(i+ 1, len(string) + 1)]
    
#     ascending_values = []

#     for substring in substrings:
#         values = []
#         for letter in substring:
#             values.append(ord(letter))

#         if values == sorted(values):
#             ascending_values.append(values)


#     longest_values = max(ascending_values, key=len)

#     final_string = ""

#     for value in longest_values:
#         final_string += chr(value)

#     return final_string