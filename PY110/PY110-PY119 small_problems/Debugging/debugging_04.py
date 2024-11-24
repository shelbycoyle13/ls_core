# You have a function that should check whether a key exists in a dictionary and returns its value. However, it's raising an error. Why is that? How would you fix this code?

# def get_key_value(my_dict, key):
#     if my_dict[key]:
#         return my_dict[key]
#     else:
#         return None

# print(get_key_value({"a": 1}, "b"))

def get_key_value(my_dict, key):
    try:
        if my_dict[key]:    #This line is redundant in a try/except block, but left there to not alter original code too much
            return my_dict[key]
    except KeyError:
            return None

print(get_key_value({"a": 1}, "b"))

# OR

# def get_key_value(my_dict, key):
#     my_dict.get(key, None)

# print(get_key_value({"a": 1}, "b"))