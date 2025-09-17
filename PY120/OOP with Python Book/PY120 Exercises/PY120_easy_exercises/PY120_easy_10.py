# Complete the Program - Houses!
# Assume you have the following code:

# class House:
#     def __init__(self, price):
#         self.price = price

#     @property
#     def price(self):
#         return self._price

#     @price.setter
#     def price(self, value):
#         self._price = value

# home1 = House(100000)
# home2 = House(150000)
# if home1 < home2:
#     print("Home 1 is cheaper")
# if home2 > home1:
#     print("Home 2 is more expensive")

# and this output:

# Home 1 is cheaper
# Home 2 is more expensive

# Modify the House class so the above program work as shown.

class House:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def __lt__(self, obj2): #Per LS Bot: using "other" as the second parameter name is a common convention, instead of my obj2
        if isinstance(obj2, House): #This checks to make sure that the second object is a House object
            return self.price < obj2.price
        
        return NotImplemented #We need to always return NotImplemented if we can't compare the two objects. LS Bot adds a comment: This signals to Python to try other approaches or to raise a TypeError is no comparison is possible
    
    def __gt__(self, obj2): #If we have a less than magic method we are editing, then we should have a greater than magic method to edit. #LS Bot says that while Python can sometimes just use one of these, using both lt and gt ensures clear and predictable comparison behavior
        if isinstance(obj2, House):
            return self.price > obj2.price
        
        return NotImplemented

home1 = House(100000)
home2 = House(150000)
if home1 < home2:
    print("Home 1 is cheaper")
if home2 > home1:
    print("Home 2 is more expensive")