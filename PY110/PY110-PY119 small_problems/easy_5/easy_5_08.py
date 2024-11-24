# Write a function that takes a string as an argument and returns that string with a staggered capitalization scheme. Every other character, starting from the first, should be capitalized and should be followed by a lowercase or non-alphabetic character. Non-alphabetic characters should not be changed, but should be counted as characters for determining when to switch between upper and lower case.

# string = 'I Love Launch School!'
# result = "I LoVe lAuNcH ScHoOl!"
# print(staggered_case(string) == result)  # True

# string = 'ALL_CAPS'
# result = "AlL_CaPs"
# print(staggered_case(string) == result)  # True

# string = 'ignore 77 the 4444 numbers'
# result = "IgNoRe 77 ThE 4444 nUmBeRs"
# print(staggered_case(string) == result)  # True

# print(staggered_case('') == "")          # True

"""
P
input = a string
output = a string
explicit = capitalize every other character
implicit = empty string should return an empty string. looks like we always start the first char as uppercase

E
# string = 'HELLO THERE'
# result = "HeLlO ThErE"
# print(staggered_case(string) == result)  # True

D
strings
looping

A
-initialize a final empty string
-iterate through each index of the string, for index of the range of the length of the string
    -if index % 2 == 0
        add string[index].upper() to final string
    else:
        add string[index].lower() to final string
-return final string
C
"""

def staggered_case(string):
    final_string = ""
    for index in range(len(string)):
        if index % 2 == 0:
            final_string += string[index].upper()
        else:
            final_string += string[index].lower()
    return final_string

string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True

string = 'HELLO THERE'
result = "HeLlO ThErE"
print(staggered_case(string) == result)  # True