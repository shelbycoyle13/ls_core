# Create a function that takes two strings as arguments and returns True if some portion of the characters in the first string can be rearranged to match the characters in the second. Otherwise, the function should return False.

# You may assume that both string arguments only contain lowercase alphabetic characters. Neither string will be empty.

# The below tests should each print True.

# print(unscramble('ansucchlohlo', 'launchschool') == True)
# print(unscramble('phyarunstole', 'pythonrules') == True)
# print(unscramble('phyarunstola', 'pythonrules') == False)
# print(unscramble('boldface', 'coal') == True)

"""
P
input = two strings
output = a Boolean
explicit = some of the characters in the first string must rearrange to match the characters in the second string; return True. else return False.
implicit = 

E


D
strings

A
-iterate through letters of second string
    -if letter not in first string
        -return False
    return True

C
"""

def unscramble(string1, string2):
    for letter in string2:
        if letter not in string1:
            return False
    
    return True

print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)