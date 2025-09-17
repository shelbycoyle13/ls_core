# Alphabet Symmetry

# Write a function that takes a list of words as input and returns a list of
# integers. Each integer represents the count of letters in the word that occupy
# their positions in the alphabet.

# Examples:
# solve(["abode","ABc","xyzD"]) # should return [4, 3, 1]
# solve(["abide","ABc","xyz"]) # should return [4, 3, 0]

"""
P
input = a list of words / strings
output = a list of integers
explicit = the characters in the words we are given have letters; those letters needs to match their respective position in the alphabet (i.e. a = 1, b = 2, c = 3)
implicit = 

E
# solve(["abcd","abe","boo"]) # should return [4, 2, 0]

D
strings
lists

A
-initialize an empty list

-for word in list
    -initialize a count to 0
    -for i, char in enumerate(word)
        char = char.lower()
        if ord(char) == i + 97:
            add +1 to count
    append count to list
    return final list
            
C
"""

def solve(lst):
    final_list = []

    for word in lst:
        count = 0
        for i, char in enumerate(word):
            char = char.lower()
            if ord(char) == i + 97:
                count += 1
        final_list.append(count)

    return final_list

print(solve(["abode","ABc","xyzD"])) # should return [4, 3, 1]
print(solve(["abide","ABc","xyz"])) # should return [4, 3, 0]
print(solve(["abcd","abe","boo"])) # should return [4, 2, 0]