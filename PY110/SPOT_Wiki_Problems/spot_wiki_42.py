# 42. Find the Parents
# Mothers arranged a dance party for the children in school. At that party, there are only mothers and their children. All are having great fun on the dance floor when suddenly all the lights went out. It's a dark night and no one can see each other. But you were flying nearby and you can see in the dark and have ability to teleport people anywhere you want.
# Legend:
# - Uppercase letters stands for mothers, lowercase stand for their children, i.e. "A" mother's children are "aaaa".
# - Function input: String contains only letters, uppercase letters are unique.

#print(find_children("abBA") == "AaBb")
#print(find_children("AaaaaZazzz") == "AaaaaaZzzz")
#print(find_children("CbcBcbaA") == "AaBbbCcc")
#print(find_children("xXfuUuuF") == "FfUuuuXx")
#print(find_children("") == "")

"""
P
input = a string
output = a string
explicit = it appears we are returning a string in alpgabetical and case order. There's only one uppercase character
implicit = empty string returns an empty string. strings should equal the same length

E

D
strings

A
we could sort the strings using sorted
return sorted string
C
"""

def alphabetical_then_upper_first(char):
    return (char.lower(), char.islower()) #This has to use .islower() and not .isupper() because in Python, False comes BEFORE True. Why? Because False = 0, True = 1!!!

def find_children(string):
    sorted_list = sorted(string, key=alphabetical_then_upper_first)

    return "".join(sorted_list)


print(find_children("abBA")  == "AaBb")
print(find_children("AaaaaZazzz") == "AaaaaaZzzz")
print(find_children("CbcBcbaA") == "AaBbbCcc")
print(find_children("xXfuUuuF") == "FfUuuuXx")
print(find_children("") == "")

#Second try, same thing but slightly different and more concisedef find_children(string):

    # list_3 = sorted(string, key=lambda letter: (letter.lower(), letter.islower()))

    # one_word = "".join(list_3)

    # return one_word