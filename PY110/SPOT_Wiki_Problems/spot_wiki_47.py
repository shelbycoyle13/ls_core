# 47. Find the missing letter
# Write a method that takes a list of consecutive (increasing) letters as input and that returns the missing letter in the list. You will always get an valid list. And it will be always exactly one letter missing. The length of the list will always be at least 2. The list will always contain letters in only one case.
# Example:
# ['a','b','c','d','f'] -> 'e'
# ['O','Q','R','S'] -> 'P'

#print(find_missing_letter(['a','b','c','d','f']) == 'e')
#print(find_missing_letter(['O','Q','R','S']) == 'P')

"""
P
input = a list (of strings)
output = a string
explicit = we want to return the missing letter. only 1 letter is missing. we're only dealing with one case.

E

D
strings
lists

A
We actually don't even need to initialize an alphabet string. We can rely on using ord() to get the Unicode values and then change it back to a letter using chr().

Iterate through the list, stopping short at the second to last element
if the ord value of the second element we are on minus the order value of the current element we are on has a difference greater than 1 when subtracting
    return the current element. Use ord() to get that value and add 1 to it. Then, use chr to get the actual character from that value

C
"""
def find_missing_letter(lst):

    for i in range(len(lst) - 1): #We use - 1 because this allows us to stop one short of the list, so we can use i + 1 below
        if ord(lst[i + 1]) - ord(lst[i]) > 1: #Difference of 2 because it's skipping over a letter
            return chr(ord(lst[i]) + 1) #We want to return the element at the current index + 1, but use ord to get the Unicode value. Then, convert the value to the actual char by using chr
        

print(find_missing_letter(['a','b','c','d','f']) == 'e')
print(find_missing_letter(['O','Q','R','S']) == 'P')


    