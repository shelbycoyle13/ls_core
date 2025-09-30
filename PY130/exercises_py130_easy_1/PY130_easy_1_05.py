# Remove None Values
# Remove all None values from a list using the filter method.

list1 = [None, "Hi", 5, None, "Hola"]

clean_list = list(filter(lambda x: x is not None, list1))

print(clean_list)

#LS Solution

# no_none = list(filter(lambda value: value is not None,
#                       [1, None, 2, None, 3, False, 4, '']))
# print(no_none)      # [1, 2, 3, False, 4, '']