# We have a list of lists and want to duplicate it. After making the copy, we modify the original list, but the copied list also seems to be affected: What's wrong here? How can you fix it?

# import copy   # The issue at hand is after making a copy of our list, we want to make a change to the original without changing the copied list.

# original = [[1], [2], [3]] 
# copied = copy.copy(original) #With copy, only the outer list is copied, but the inner lists are shared.

# original[0][0] = 99

# print(copied[0] == [1])

import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original) # To keep these separate, use deepcopy

original[0][0] = 99

print(copied[0] == [1])