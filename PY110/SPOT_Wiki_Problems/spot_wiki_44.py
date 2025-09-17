# 44. Squared Array Check
# Given two lists a and b, write a function comp(a, b) that checks whether the two lists have the "same" elements, with the same multiplicities.
# "Same" means, here, that the elements in `b` are the elements in `a` squared, regardless of the order.

#print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]) == True)
#print(comp([121, 144, 19, 161, 19, 144, 19, 11], [132, 14641, 20736, 361, 25921, 361, 20736, 361]) == False)
#print(comp(None, [1, 2, 3]) == False)
#print(comp([1, 2], []) == False)
#print(comp([1, 2], [1, 4, 4]) == False)

"""
P
input = two lists
output = a Boolean
explicit = we want to check that the squared numbers in the A list are in the B list. Order doesn't matter.
implicit = None is possible as an A list argument. Empty lists are possible as a B list.

E

D
lists

A
if the first argument is None
    return False
if the second argument is False
    return False
i want to iterate through the A list. for every number in the set of A list
    square the number
    check if the squared number matches the same count of squared numbers in the B list
    otherwise return False

C
"""
def comp(lstA, lstB):
    if lstA is None or lstB is None:
        return False
    
    for num in set(lstA):
        if lstA.count(num) != lstB.count(num**2):
            return False
    return True

print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]) == True)
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [132, 14641, 20736, 361, 25921, 361, 20736, 361]) == False)
print(comp(None, [1, 2, 3]) == False)
print(comp([1, 2], []) == False)
print(comp([1, 2], [1, 4, 4]) == False)