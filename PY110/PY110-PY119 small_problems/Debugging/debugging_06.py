# We want to create a function that appends a given value to a list. However, the function seems to be behaving unexpectedly:
# How would you fix this code?

# def append_to_list(value, lst=[]):   # In this example, the parameter lst is a mutable argument. Default mutable arguments are shared
#     lst.append(value)     # between function calls. So we used the same list again when we called the function a second time.
#     return lst

# print(append_to_list(1) == [1])
# print(append_to_list(2) == [2]) # This was False because it was returning [1, 2]

def append_to_list(value):
    lst = [] # Here I moved the lst inside the function body so we get a new lst every time we call the function
    lst.append(value)
    return lst

# OR

# def append_to_list(value, lst=None): #In the LS solution, here we still have lst as a parameter but with a default value of None
#     if lst is None:
#         lst = []

#     lst.append(value)
#     return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])