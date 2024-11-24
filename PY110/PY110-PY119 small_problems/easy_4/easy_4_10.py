# Building on the previous exercise, write a function that returns True or False based on whether or not an inventory item (an ID number) is available. As before, the function takes two arguments: an item ID and a list of transactions. The function should return True only if the sum of the quantity values of the item's transactions is greater than zero. Notice that there is a movement property in each transaction object. A movement value of 'out' will decrease the item's quantity.

# You may (and should) use the transactions_for function from the previous exercise.

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

# print(is_item_available(101, transactions) == False)  # True
# print(is_item_available(103, transactions) == False)  # True
# print(is_item_available(105, transactions) == True)   # True

"""
P
input = an integer and a variable that references a list of dictionaries
output = a Boolean
explicit = we return True if the quanitity of an item is greater than 0. If movement is "out", we decrease that from the quantity of the item. we can use our function from the previous exercise.
implicit = quanitity can be negative

E
# print(is_item_available(102, transactions) == False)  # True

D
lists
dictionaries

A
-our previous function returns the dictionaries for a particuar id number
-for this id number, if a "movement" shows "in", we should add
-if a "movement" shows "out", we should subtract

C
"""

def transactions_for(id, lst):
    # for dict in lst:
    #     for value in dict.values():
    #         if value == id:
    #             return dict
            
    return [dict for dict in lst
            for value in dict.values()
            if value == id]

def is_item_available(id, lst):
    total_quantity = 0

    for dictionary in transactions_for(id, lst):
        if dictionary["movement"] == "in":
            total_quantity += dictionary["quantity"]
        else:
            total_quantity -= dictionary["quantity"]
    
    if total_quantity > 0:
        return True
    return False

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True
print(is_item_available(102, transactions) == False)  # True