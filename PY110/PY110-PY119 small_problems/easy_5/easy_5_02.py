# Given a dictionary and a list of keys, produce a new dictionary that only contains the key/value pairs for the specified keys.
    
#     input_dict = {
#     'red': 1,
#     'green': 2,
#     'blue': 3,
#     'yellow': 4,
# }

# keys = ['red', 'blue']
# expected_dict = {'red': 1, 'blue': 3}
# print(keep_keys(input_dict, keys) == expected_dict) # True

"""
P
input = a dictionary and a list of keys
output = a new dictionary
explicit = the new dict only contains keys that are asked for
implicit = 

E
#     input_dict = {
#     'orange': 4,
#     'purple': 3,
#     'pink': 2,
#     'periwinkle': 1,
# }

# keys = ['purple', 'pink']
# expected_dict = {'purple': 3, 'pink': 2}
# print(keep_keys(input_dict, keys) == expected_dict) # True


D
dictionaries
lists

A
-initialize a new empty dict
-for keys and values in dict
    - if key in keys
        - add key, value to new dict
return new dict

C
"""

def keep_keys(dictionary, lst):
    # new_dict = {}
    # for key, value in dictionary.items():
    #     if key in lst:
    #         new_dict[key] = value

    # return new_dict
            
    return {key:value for key, value in dictionary.items() if key in lst}

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True

input_dict = {
    'orange': 4,
    'purple': 3,
    'pink': 2,
    'periwinkle': 1,
}

keys = ['purple', 'pink']
expected_dict = {'purple': 3, 'pink': 2}
print(keep_keys(input_dict, keys) == expected_dict) # True