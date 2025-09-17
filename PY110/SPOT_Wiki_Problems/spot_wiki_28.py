# 28. Group by 2 chars
# # Write a function that splits the string into pairs of two characters.
# # If the string contains an odd number of characters, replace the missing second character of the final pair with an underscore ('_').

#solution('abc') == ['ab', 'c_']
#solution('abcdef') == ['ab', 'cd', 'ef']
#solution("abcdef") == ["ab", "cd", "ef"]
#solution("abcdefg") == ["ab", "cd", "ef", "g_"]
#solution("") == []

"""
P
input = 1 string
output = a list of strings
explicit = we want to split the string into pairs of letters. if we're dealing with a list that has an odd length, have the last letter be an underscore
implicit = an empty string = an empty list

E

D
lists
strings

A
-new_list = []
iterate through the string, for i, letter in enumerate(string)
    -pair = ""
    -pair += letter
    -if len of string is odd and i == -1: ###### WE CAN'T USE -1 LIKE THIS BECAUSE -1 DOESN'T HAPPEN NATURALLY DURING ITERATION
        -add _ to pair
    -if pair's length == 2
        -append pair to new list

-return new list


C
"""
def solution(string):
    final_list = []
    pair = ""

    for i, letter in enumerate(string):
        pair += letter
        if len(pair) == 2:
            final_list.append(pair)
            pair = ""

    if len(pair) == 1: #We had to check if pair was only a length of 1 at the end of the other loop. This is the same as checking if the length is odd
        pair += "_"
        final_list.append(pair)
    
    return final_list

print(solution('abc') == ['ab', 'c_'])
print(solution('abcdef') == ['ab', 'cd', 'ef'])
print(solution("abcdef") == ["ab", "cd", "ef"])
print(solution("abcdefg") == ["ab", "cd", "ef", "g_"])
print(solution("") == [])