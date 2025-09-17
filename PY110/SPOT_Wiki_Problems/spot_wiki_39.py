# 39. Sort Arrays (Case-Insensitive)
# Sort the given strings in alphabetical order, case insensitive.

#print(sortme(["Hello", "there", "I'm", "fine"]) == ["fine", "Hello", "I'm", "there"])
#print(sortme(["C", "d", "a", "Ba", "be"]) == ["a", "Ba", "be", "C", "d"])

"""
P
input = a list
output = a list
explicit = we want to sort the list in alphabetical order. Case is irrelevant
implicit = the rules don't say if we want to return a new list or not

E

D
lists
strings

A
using the sort function should sort strings in alphabetical order

C
"""
def lowercase(string):
    return string.lower()

def sortme(lst):
    lst.sort(key=lowercase) #lst.sort also uses keys for custom sorting
    return lst #But you have to return the lst on it's own on a separate line since returning .sort returns None

    #OR

    return sorted(lst, key=lowercase) #To return a new list, and can return in one line

print(sortme(["Hello", "there", "I'm", "fine"]) == ["fine", "Hello", "I'm", "there"])
print(sortme(["C", "d", "a", "Ba", "be"]) == ["a", "Ba", "be", "C", "d"])