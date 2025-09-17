# # 15. Take a Walk
# You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- every time you press the button it sends you a list of one-letter strings representing directions to walk (e.g., ['n', 's', 'w', 'e']). You always walk only a single block in a direction, and you know it takes you one minute to traverse one city block. Create a function that will return `True` if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return `False` otherwise.

# Note: You will always receive a valid list containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty list (that's not a walk, that's standing still!).

# Examples:
# is_valid_walk(['n','s','n','s','n','s','n','s','n','s']) # should return True
# is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']) # should return False
# is_valid_walk(['w']) # should return False
# is_valid_walk(['n','n','n','s','n','s','n','s','n','s']) # should return False

"""
P
input = a list 
output = a Boolean
explicit = first condition is that the list contains letters of only n s e w. Each walk should only take 10 min, so we should only have 10 letters. Finally, the directions should lead you back to where you started. so number of N = number of S; number of E = number of W.
implicit = 

E

D
lists
strings

A
-if length doesn't == 10
    -return False
elif:
    -lst.count(n) == lst.count(s) and lst.count(e) == lst.count(w)
        -return True
else:
    -return False

C
"""
def is_valid_walk(lst):
    if len(lst) != 10:
        return False
    elif lst.count("n") == lst.count("s") and lst.count("e") == lst.count("w"):
        return True
    else:
        return False
    
print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']) == True) # should return True
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']) == False) # should return False
print(is_valid_walk(['w']) == False) # should return False
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']) == False) # should return False