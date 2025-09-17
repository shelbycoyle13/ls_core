# Only Pass the Year
# Using the following code, modify Truck to accept a second argument when instantiating a new Truck object. Name the parameter bed_type. Ensure that the Car constructor continues to accept only one argument.

class Vehicle:
    def __init__(self, year):
        self._year = year

    @property
    def year(self):
        return self._year

class Truck(Vehicle):
    def __init__(self, year, bed_type):
        super().__init__(year) #Since this is the same from the superclass, we want to use the super function, call the init method, and pass in the year. This is another way of saying we want to access the superclass, call its initializer, and pass in the year argument to the superclass' method
        self._bed_type = bed_type

    @property
    def bed_type(self): #We created this property method since we see this method being called in the print statements below
        return self._bed_type

class Car(Vehicle):
    pass #No need to put anything here yet. We want the error to be raised as is by Python and displayed in the terminal

# Comments show expected output
truck1 = Truck(1994, 'Short')
print(truck1.year)            # 1994
print(truck1.bed_type)        # Short

car1 = Car(2006)
print(car1.year)              # 2006
print(car1.bed_type)
# AttributeError: 'Car' object has no attribute 'bed_type'

