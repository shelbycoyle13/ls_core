# Modify the function from the previous exercise so it ignores non-alphabetic characters when determining whether it should uppercase or lowercase each letter. The non-alphabetic characters should still be included in the return value; they just don't count when toggling the desired case.

# string = 'I Love Launch School!'
# result = "I lOvE lAuNcH sChOoL!"
# print(staggered_case(string) == result)  # True

# string = 'ALL_CAPS'
# result = "AlL_cApS"
# print(staggered_case(string) == result)  # True

# string = 'ignore 77 the 4444 numbers'
# result = "IgNoRe 77 ThE 4444 nUmBeRs"
# print(staggered_case(string) == result)  # True

# print(staggered_case('') == "")          # True

"""
P
input = string
output = string (with alternating cases, but skipping whitespace)
explicit = we're ignoring whitespace, meaning the next character is still the opposite case of the previous character
implicit = empty strings return empty strings

E


D
strings
looping

A
# string = 'Pizza rules!'
# result = "PiZzA rUlEs"
# print(staggered_case(string) == result)  # True

C
"""

def staggered_case(string):
    final_string = ""
    upper = True
    for char in string:
        if char.isalpha():
            if upper:
                final_string += char.upper()
            else:
                final_string += char.lower()
            upper = not upper # If the character is alphabetic, after adding the character to the string, it will toggle between True and False
        else:
            final_string += char
    return final_string

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True

string = 'Pizza rules!'
result = "PiZzA rUlEs!"
print(staggered_case(string) == result)  # True