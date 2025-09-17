# Refactoring Vehicles
# Consider the following classes:

# class Car:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def get_wheels(self):
#         return 4

#     def info(self):
#         return f"{self.make} {self.model}"

# class Motorcycle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def get_wheels(self):
#         return 2

#     def info(self):
#         return f"{self.make} {self.model}"

# class Truck:
#     def __init__(self, make, model, payload):
#         self.make = make
#         self.model = model
#         self.payload = payload

#     def get_wheels(self):
#         return 6

#     def info(self):
#         return f"{self.make} {self.model}"

# Refactor these classes so they all use a common superclass, and inherit behavior as needed.

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_wheels(self, total_wheels): #LS Suggests to just keep the get_wheels as is in the original code. My solution makes for unnecessary parameters, instance variable storage, and simply making the code cleaner and straightforward.
        self.total_wheels = total_wheels
        return self.total_wheels
    
    def info(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def get_wheels(self):
        return super().get_wheels(4)

class Motorcycle(Vehicle):
    def get_wheels(self):
        return super().get_wheels(2)

class Truck(Vehicle):
    def __init__(self, make, model, payload):
        self.payload = payload
        super().__init__(make, model) #It's actually convention to have this line be first rather than the creation of the next instance variable, in this case, self.payload. LS Bot says this ensures parent class initialization before any additional subclass specific setup. This order ensures that the object is properly initialized in the expected sequence.

    def get_wheels(self):
        return super().get_wheels(6)

honda_CRV = Car("Honda", "CRV")
print(honda_CRV.info())
print(honda_CRV.get_wheels())

harley = Motorcycle("Harley Davidson", "Low Rider")
print(harley.info())
print(harley.get_wheels())

mack = Truck("Mack", "Anthem", 50000)
print(mack.info())
print(mack.get_wheels())
print(mack.payload)