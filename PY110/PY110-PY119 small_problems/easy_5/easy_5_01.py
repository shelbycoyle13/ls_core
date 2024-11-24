# Given a dictionary where both keys and values are unique, invert this dictionary so that its keys become values and its values become keys.

# print(invert_dict({
#           'apple': 'fruit',
#           'broccoli': 'vegetable',
#           'salmon': 'fish',
#       }) == {
#           'fruit': 'apple',
#           'vegetable': 'broccoli',
#           'fish': 'salmon',
#       })  # True

"""
P
input = a dictionary
output = a dictionary
explicit = we are swapping the keys' placement for the values' placement and vice versa
implicit = 

E
# print(invert_dict({
#           'red': 'color',
#           'parrot': 'bird',
#           'tabby': 'cat',
#       }) == {
#           'color': 'red',
#           'bird': 'parrot',
#           'cat': 'tabby',
#       })  # True

D
dictionaries

A
-for each key and value in the dictionary
    key = value and value = key
return the dictionary
C
"""

def invert_dict(dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        new_dict[value] = key
    return new_dict

# # Practice with a dictionary comprehension:

#     return {value:key for key, value in dictionary.items()}

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True

print(invert_dict({
          'red': 'color',
          'parrot': 'bird',
          'tabby': 'cat',
      }) == {
          'color': 'red',
          'bird': 'parrot',
          'cat': 'tabby',
      })  # True