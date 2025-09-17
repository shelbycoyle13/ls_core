# 33. Find the Suspect

# # Sherlock has to find suspects on his latest case. He will use your method. Suspect in this case is a person which has something not allowed in his/her pockets.  Allowed items are defined by an list of numbers. Pockets contents are defined by map entries where key is a person and value is one or few things represented by a list of numbers (can be nil or empty list if empty).

# pockets = {
#     'bob': [1],
#     'tom': [2, 5],
#     'jane': [7]
# }

#print(find_suspects(pockets, [1, 2]) == ['tom', 'jane'])
#print(find_suspects(pockets, [1, 7, 5, 2]) == None))
#print(find_suspects(pockets, []) == ['bob', 'tom', 'jane'])
#print(find_suspects(pockets, [7]) == ['bob', 'tom'])

"""
P
input = a dict, a list
output = strings, or None
explicit = the list argument represents the allowed items. we want to return the names of the suspects that are associated with the other numbers
implicit = if our list argument has every number, return None. If list argument is empty, return all names

E

D
dict
strings

A
if list argument is empty
    return None
else:
suspect_list = []
    iterate through the dict, for key, value in dict.items
        if value not in list argument
            suspect_list.append(key)

return suspect_list

C
"""
pockets = {
    'bob': [1],
    'tom': [2, 5],
    'jane': [7]
}

def find_suspects(dict1, lst):
    if len(lst) == 0: #If we have an empty list
        return list(dict1.keys()) #Just return a list of every key fgrom the dict, everyone is a suspect
    else: #Otherwise
        suspect_list = [] #Start with an empty list
        for key, values in dict1.items(): #Iterate through the key value pairs in the dict
            for value in values: #Because the values are also lists, we have to iterate though them to get just the numbers
                if value not in lst: #If the dict value is not in the list argument of allowed items
                    suspect_list.append(key) #That means this person has something that doesn't belong to them, i.e. they're a suspect
                    break #We only need to add them to the list once, not multiple times for multiple items they may have

        return suspect_list if suspect_list else None #We can return a conditional expression like this. Return the suspect list if it's truthy, otherwise, return None

print(find_suspects(pockets, [1, 2]) == ['tom', 'jane'])
print(find_suspects(pockets, [1, 7, 5, 2]) == None)
print(find_suspects(pockets, []) == ['bob', 'tom', 'jane'])
print(find_suspects(pockets, [7]) == ['bob', 'tom'])