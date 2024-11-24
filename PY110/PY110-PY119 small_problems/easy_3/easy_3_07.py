# Write a function that takes a string argument consisting of a first name, a space, and a last name. The function should return a new string consisting of the last name, a comma, a space, and the first name.

# You may assume that the names don't include middle names, initials, or suffixes ("Jr.", "Sr.").

# print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

"""
P
input = string
output = string
explicit = first name space last name -> last name comma first name
implicit = i'm assuming there are no two "first names" i.e. mary jane roberts

E
# print(swap_name('Shelby Coyle') == "Coyle, Shelby")   # True

D
possible looping
possible slicing

A
-let's take our original string and split by the whitespace
- now we have a list of two strings
- initialize a new final string
- concatenate the 2nd element, a comma, space, and the first element to the new final string

C
"""

def swap_name(name):
    final_string = ""
    name_list = name.split()
    not_last_name = name_list[:-1]
    final_string += name_list[-1] + ", " + " ".join(not_last_name)
    return final_string

print(swap_name('Joe Roberts') == "Roberts, Joe")
print(swap_name('Shelby Coyle') == "Coyle, Shelby")
print(swap_name('Mary Jane Watson') == "Watson, Mary Jane") 