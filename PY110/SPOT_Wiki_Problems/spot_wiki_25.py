# 25. How many cakes can the baker make?
# # Pete is baking cakes and needs help calculating how many he can make with his recipes and available ingredients.
# # Write a function cakes() that takes two dictionaries: the recipe and the available ingredients. Return the maximum number of cakes Pete can bake.

# # Rules:
# # - Ingredients not present in the objects can be considered as 0.

# # must return 2
# cakes({"flour":500, "sugar":200, "eggs":1},{"flour":1200, "sugar":1200, "eggs":5, "milk":200}) == 2

# # must return 11
# cakes({"cream":200, "flour":300, "sugar":150, "milk":100, "oil":100},{"sugar":1700, "flour":20000,
# "milk":20000, "oil":30000, "cream":5000}) == 11

# # must return 0
# cakes({"apples":3, "flour":300, "sugar":150, "milk":100, "oil":100},{"sugar":500, "flour":2000,
# "milk":2000}) == 0

# # must return 0
# cakes({"apples":3, "flour":300, "sugar":150, "milk":100, "oil":100},{"sugar":500, "flour":2000,
# "milk":2000, "apples":15, "oil":20}) == 0

# # must return 0
# cakes({"eggs":4, "flour":400},{}) == 0

# # must return 1
# cakes({"cream":1, "flour":3, "sugar":1, "milk":1, "oil":1, "eggs":1},{"sugar":1, "eggs":1, "flour":3,
# "cream":1, "oil":1, "milk":1}) == 1

"""
P
input = 2 dictionaries
output = 1 integer
explicit = we are first passing in the recipe, then our ingredients. we want to return how many cakes we can make with the ingredients we have. if we are missing any ingredients, we can't make the cake, and must return 0. the amount for any missing ingredients is 0.
implicit = 

E

D
dictionaries

A
-make a list to extract keys from recipe
-make a list to extract keys from ingredients
-if keys are not the same in both
    -return False
-else
    -divide the values from ingredients with values from recipe - while loop
    -need a quotient for all key/value pairs
    -return the minimum quotient

C
"""

def cakes(recipe, inventory):

    cakes_per_ingredient = [] #we're initializing an empty list because we want to store the amount of cakes we can make per ingredient
    
    for ingredient, required_amount in recipe.items(): #Looping through each key/value pair in the recipe

        available_amount = inventory.get(ingredient, 0) #For every item in the recipe, we want to calculate the amount we have per item. If that item doesn't exist in our inventory, set a default value to 0

        if available_amount < required_amount: #If what we have is less than the amount we need, return 0
            return 0
        
        cakes_per_ingredient.append(available_amount // required_amount) #Let's divide what we have by the amount we need. That number is equal to the amount of cakes we can make per ingredient. Append this number to our list

    return min(cakes_per_ingredient) #We want to return the minimum number in that list as that represents the minimum amount of cakes we can make given our ingredient amounts
        
            

 # must return 2
print(cakes({"flour":500, "sugar":200, "eggs":1},{"flour":1200, "sugar":1200, "eggs":5, "milk":200}) == 2)

# must return 11
print(cakes({"cream":200, "flour":300, "sugar":150, "milk":100, "oil":100},{"sugar":1700, "flour":20000,
"milk":20000, "oil":30000, "cream":5000}) == 11)

# must return 0
print(cakes({"apples":3, "flour":300, "sugar":150, "milk":100, "oil":100},{"sugar":500, "flour":2000,
"milk":2000}) == 0)

# must return 0
print(cakes({"apples":3, "flour":300, "sugar":150, "milk":100, "oil":100},{"sugar":500, "flour":2000,
"milk":2000, "apples":15, "oil":20}) == 0)

# must return 0
print(cakes({"eggs":4, "flour":400},{}) == 0)

# must return 1
print(cakes({"cream":1, "flour":3, "sugar":1, "milk":1, "oil":1, "eggs":1},{"sugar":1, "eggs":1, "flour":3,
"cream":1, "oil":1, "milk":1}) == 1)