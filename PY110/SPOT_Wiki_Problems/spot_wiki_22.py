# 22. Substring is Anagram?
# Write a function `scramble(str1, str2)` that returns `True` if a portion of
# `str1` characters can be rearranged to match `str2`, otherwise returns `False`.

# Notes:
# - Only lower case letters will be used (a-z). No punctuation or digits will
# 	be included.
# - Performance needs to be considered.
# - Input strings `str1` and `str2` are null terminated.

# Examples:
# scramble('rkqodlw', 'world') # should return True
# scramble('cedewaraarossoqqyt', 'carrot') # should return True
# scramble('katas', 'steak') # should return False
# scramble('scriptjava', 'javascript') # should return True
# scramble('scriptingjava', 'javascript') # should return True

"""
P
input = two strings
output = a Boolean
explicit = all of string2 needs to be in string1
implicit = 

E

D
strings

A
-for letter in str2
    -if str2.count(letter) =< str1.count(letter)
        -return True

C
"""

def scramble(str1, str2):
    for letter in str2:
        if str2.count(letter) > str1.count(letter): #Sometimes you have to reverse your logic. If this goes the entire loop without satisfying the opposite condition, then it'll return True (i.e. "This is an anagram after all!"). Make a function stop anf return False as soon as it doesn't match your condition. 
            return False
    return True

print(scramble('rkqodlw', 'world') == True)# should return True
print(scramble('cedewaraarossoqqyt', 'carrot') == True)# should return True
print(scramble('katas', 'steak') == False)# should return False
print(scramble('scriptjava', 'javascript') == True)# should return True
print(scramble('scriptingjava', 'javascript') == True)# should return True