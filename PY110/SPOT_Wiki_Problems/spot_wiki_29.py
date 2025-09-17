# 29. Anagram Difference Count

# # Given two words, determine the number of letters you need to remove from them to make them anagrams.

#print(anagram_difference('', '') == 0)
#print(anagram_difference('a', '') == 1)
#print(anagram_difference('', 'a') == 1)
#print(anagram_difference('ab', 'a') == 1)
#print(anagram_difference('ab', 'ba') == 0)
#print(anagram_difference('ab', 'cd') == 4)
#print(anagram_difference('aab', 'a') == 2)
#print(anagram_difference('a', 'aab') == 2)

"""
P
input = 2 strings
output = an integer
explicit = we want return the integer that represents the difference between two strings to make them anagrams
implicit = if the two string arguments given are already anagrams then return 0. if the two string arguments are empty, also return 0.

E

D
strings


A
if sorted(string1) == sorted(string2):
    return 0

total_difference = 0

-iterate through the first string, for letter in set(string1)
    -difference = abs(string1.count(letter) - string2.count(letter))
    -total_difference += difference

-iterate through the second string, for letter in set(string2)
    -difference = abs(string2.count(letter) - string1.count(letter))
    -total_difference += difference

return total_difference

C
"""
def anagram_difference(string1, string2):
    
    total_difference = 0

    for letter in set(string1) | set(string2):
        difference = abs(string1.count(letter) - string2.count(letter))
        total_difference += difference

    return total_difference

print(anagram_difference('', '') == 0)
print(anagram_difference('a', '') == 1)
print(anagram_difference('', 'a') == 1)
print(anagram_difference('ab', 'a') == 1)
print(anagram_difference('ab', 'ba') == 0)
print(anagram_difference('ab', 'cd') == 4)
print(anagram_difference('aab', 'a') == 2)
print(anagram_difference('a', 'aab') == 2)