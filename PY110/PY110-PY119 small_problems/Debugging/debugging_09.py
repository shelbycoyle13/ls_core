# We want to remove certain items from a set while iterating over it, but the code below throws an error. Why is that and how can we fix it?

# data_set = {1, 2, 3, 4, 5}

# for item in data_set:
#     if item % 2 == 0:
#         data_set.remove(item) #The problem is we can't change the size of the set while iterating over it. This also goes for frozen sets as well

data_set = {1, 2, 3, 4, 5}
new_set = set() # I just made a new set
for item in data_set:
    if item % 2 != 0: # And negated the original condition. If the number is odd, add it to the new set
        new_set.add(item)

# OR - let's practice with a set comprehension

# new_set = {item for item in data_set
#             if item % 2 != 0}

print(new_set)