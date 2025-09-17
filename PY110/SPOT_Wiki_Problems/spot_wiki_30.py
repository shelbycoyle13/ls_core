# 30. Is anagram?
# # Write a function to determine if two words are anagrams of each other.

#print(is_anagram('Creative', 'Reactive') == True)
#print(is_anagram("foefet", "toffee") == True)
#print(is_anagram("Buckethead", "DeathCubeK") == True)
#print(is_anagram("Twoo", "WooT") == True)
#print(is_anagram("dumble", "bumble") == False)

"""
P
input = two strings
output = a Boolean
explicit = we want to check if each string is an anagram of each other
implicit = looks like case is irrelevant

E

D
strings

A
-if we sort each string AND turn them into lowercase characters, then they are anagrams of each other

C
"""
def is_anagram(string1, string2):

    if sorted(string1.lower()) == sorted(string2.lower()):
        return True
    return False
    
print(is_anagram('Creative', 'Reactive') == True)
print(is_anagram("foefet", "toffee") == True)
print(is_anagram("Buckethead", "DeathCubeK") == True)
print(is_anagram("Twoo", "WooT") == True)
print(is_anagram("dumble", "bumble") == False)