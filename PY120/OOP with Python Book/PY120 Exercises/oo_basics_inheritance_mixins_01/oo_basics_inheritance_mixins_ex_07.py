# TowingMixin (Part 2)
# Given the following code, create a class named Vehicle that, upon instantiation, assigns the passed-in argument to self.year. Both Truck and Car should inherit from Vehicle.

class TowingMixin:
    def tow(self):
        return 'I can tow a trailer!'
    
class Vehicle:
    def __init__(self, year):
        self.year = year

class Truck(TowingMixin, Vehicle): #We want to list the mixin first in our parameters to make sure the methods in the mixin get found before those in the superclass. The MRO would change if Vehicle was before the mixin - that's not what we want. It's a convention to put mixins first!
    pass

class Car(Vehicle):
    pass

# Comments show expected output
truck1 = Truck(1994)
print(truck1.year)            # 1994
print(truck1.tow())           # I can tow a trailer!

car1 = Car(2006)
print(car1.year)              # 2006