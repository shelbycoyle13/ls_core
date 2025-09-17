# # 20. Character Count Sorting
# Write a function that takes a string as an argument and groups the
# number of times each character appears in the string as a dictionary
# sorted by the highest number of occurrences.

# The characters should be sorted alphabetically, and you should ignore
# spaces, special characters, and count uppercase letters as lowercase ones.

# Examples:
# get_char_count("Mississippi") # should return {4: ['i', 's'], 2: ['p'], 1: ['m']}
# get_char_count("Hello. Hello? HELLO!!") # should return {6: ['l'], 3: ['e', 'h', 'o']}
# get_char_count("aaa...bb...c!") # should return {3: ['a'], 2: ['b'], 1: ['c']}
# get_char_count("aaabbbccc") # should return {3: ['a', 'b', 'c']}
# get_char_count("abc123") # should return {1: ['1', '2', '3', 'a', 'b', 'c']}

"""
P
input = a string
output = a dictionary
explicit = we want to count the number of occurrences of each letter and number, add them to a dictionary. dict should have the number of occurences sorted. if there are ties, then sort alphabetically. keys are integers, values are lists
implicit = 

E

D
strings
dict
list

A
initialize empty dict
-iterate through the string, for char in string.lower
    -if char not in dict, add it as a key
    -else
        dict[key] += 1

sorted_dict = sorted(dict.values, reverse = True)

{value: [key] for key, values in sorted_dict_values}

C
"""

def get_char_count(string):

    new_dict = {}

    for char in string.lower():
        if not char.isalnum():
            continue
        if char not in new_dict:
            new_dict[char] = 1
        else:
            new_dict[char] += 1

    grouped_counts = {}
    for char, count in new_dict.items(): # Group characters by their counts
        grouped_counts.setdefault(count, []).append(char) #setdefault returns the value of the key if it exists, otherwise we set and return a default value

    for count in grouped_counts:
        grouped_counts[count].sort() #This sorts the values / letters alphabetically in the list

    sorted_dict = {count: grouped_counts[count] for count in sorted(grouped_counts, reverse=True)}

    return sorted_dict

print(get_char_count("Mississippi") == {4: ['i', 's'], 2: ['p'], 1: ['m']}) # should return {4: ['i', 's'], 2: ['p'], 1: ['m']}
print(get_char_count("Hello. Hello? HELLO!!") == {6: ['l'], 3: ['e', 'h', 'o']}) # should return {6: ['l'], 3: ['e', 'h', 'o']}
print(get_char_count("aaa...bb...c!") == {3: ['a'], 2: ['b'], 1: ['c']}) # should return {3: ['a'], 2: ['b'], 1: ['c']}
print(get_char_count("aaabbbccc") == {3: ['a', 'b', 'c']}) # should return {3: ['a', 'b', 'c']}
print(get_char_count("abc123") == {1: ['1', '2', '3', 'a', 'b', 'c']}) # should return {1: ['1', '2', '3', 'a', 'b', 'c']}