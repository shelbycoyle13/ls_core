# Write a function that finds all the anagrams of a word from a list.
# Two words are anagrams of each other if they both contain the same letters.

# Examples
# 'abba' & 'baab' == true
# 'abba' & 'bbaa' == true
# 'abba' & 'abbba' == false
# 'abba' & 'abca' == false

# print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa'])
# print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer'])
# print(anagrams('laser', ['lazing', 'lazy', 'lacer']) == [])

"""
P
input = 1 string, and 1 list of strings
output = 1 list of strings which contain strings that are anagrams of the string argument
explicit = we want to find the matching anagrams from the lis argument that match the string argument
implicit = the list of strings (argument) can contain letters in strings that have nothing to do with the 1st string argument. if the list argument has no strings that are anagrams of the string argument, return an empty list

E

D
strings
lists

A

-initialize anagrams list

-for string in list
    -for letter in string
        -if letter not in string argument
            -break
    -append string to new list


C
"""

def anagrams(string_arg, lst):

    anagrams_list = []

    for string in lst:
        if sorted(string) == sorted(string_arg): #Such a simple solution! Think: Anagrams are just unsorted strings! So SORT THEM!
            anagrams_list.append(string)

    return anagrams_list

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa'])
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer'])
print(anagrams('laser', ['lazing', 'lazy', 'lacer']) == [])