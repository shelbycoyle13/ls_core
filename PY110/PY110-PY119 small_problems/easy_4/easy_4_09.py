# Write a function that takes two arguments, an inventory item ID and a list of transactions, and returns a list containing only the transactions for the specified inventory item.

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

# print(transactions_for(101, transactions) ==
#       [
#           {"id": 101, "movement": "in",  "quantity":  5},
#           {"id": 101, "movement": "in",  "quantity": 12},
#           {"id": 101, "movement": "out", "quantity": 18},
#       ]) # True


"""
P
input = 2 arguments, an integer and a variable that points to a list of dictionaries
output = a list of dictionaries
explicit = we only want the returned list to have dictionaries that include the id we're looking for
implicit = 

E
print(transactions_for(103, transactions)) == 
    [{"id": 103, "movement": 'out', "quantity": 20},
    {"id": 103, "movement": 'out', "quantity": 15}
    ]

D
lists
dictionaries

A
-for the list that is passed in, we want to identify the values in the dictionaries first.

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

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True

print(transactions_for(103, transactions) == [{"id": 103, "movement": 'out', "quantity": 20}, {"id": 103, "movement": 'out', "quantity": 15}])