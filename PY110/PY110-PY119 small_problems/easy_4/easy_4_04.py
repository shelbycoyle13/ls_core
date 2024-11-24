# Given a dictionary, return its keys sorted by the values associated with each key.

# my_dict = {'p': 8, 'q': 2, 'r': 6}
# keys = ['q', 'r', 'p']
# print(order_by_value(my_dict) == keys)  # True

"""
P
input = a dictionary
output = a list (of just the keys)
explicit = we are sorting in ascending order
implicit = 

E
# my_dict = {'p': 3, 'q': 2, 'r': 1}
# keys = ['r', 'q', 'p']
# print(order_by_value(my_dict) == keys)  # True

D
dictionaries
lists
dictionary view objects
helper function

A
-use the .items() method to get the dictionary view object
-use this in a helper function
- we want to unpack the tuples and return just the values
-in our main function, use sorted on the dictionary and use the return value of the helper function as the key
-return the keys in a list

C
"""


def order_by_value(dictionary):

    dict_list_tuples = list(dictionary.items())
    
    def sort_by_values(pair):
        letter, value = pair
        return value, letter
    
    sorted_by_values = sorted(dict_list_tuples, key=sort_by_values)
    
    ascending_letters = [letter for letter, value in sorted_by_values]
    return ascending_letters

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True

my_dict = {'p': 3, 'q': 2, 'r': 1}
keys = ['r', 'q', 'p']
print(order_by_value(my_dict) == keys)  # True