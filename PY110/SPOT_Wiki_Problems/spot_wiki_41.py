# 41. Counting Duplicates
# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string.

#print(duplicate_count("") == 0)
#print(duplicate_count("abcde") == 0)
#print(duplicate_count("abcdeaa") == 1)
#print(duplicate_count("abcdeaB") == 2)
#print(duplicate_count("Indivisibilities") == 2)

"""
P
input = a string
output = an integer
explicit = we want to return the number of characters that occur more than once. case is irrelevant
implicit = empty string = 0

E

D
strings

A
count = 0
iterate though the lowercase version of the string, for char in string
    if char count is greater than 1
        add 1 to the count

return count

C
"""

def duplicate_count(string):
    total_count = 0

    for char in set(string.lower()):
        if string.lower().count(char) > 1:
            total_count += 1

    return total_count


print(duplicate_count("") == 0)
print(duplicate_count("abcde") == 0)
print(duplicate_count("abcdeaa") == 1)
print(duplicate_count("abcdeaB") == 2)
print(duplicate_count("Indivisibilities") == 2)