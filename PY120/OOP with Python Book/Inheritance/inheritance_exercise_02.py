# 2. Write the code needed to make the following code work as shown:

# print(Car.vehicles())     # 0
# car1 = Car()
# print(Car.vehicles())     # 1
# car2 = Car()
# car3 = Car()
# car4 = Car()
# print(Car.vehicles())     # 4
# truck1 = Truck()
# truck2 = Truck()
# print(Truck.vehicles())   # 6
# boat1 = Boat()
# boat2 = Boat()
# print(Boat.vehicles())    # 8

class Vehicle:
    number_of_vehicles = 0 #We should initialize this in the superclass

    def __init__(self): #We should have this by default
        Vehicle.number_of_vehicles += 1 #Why do we put the class name here? We put the class name here to ensure we are modifying the variable in the Vehicle class, not in any potential subclass

    @classmethod
    def vehicles(cls): #Why do we need to create this? Why not just return this in the class Vehicles or in the init method? Init should only be focused on initializing the object, not returning data.  Creating this method provides an interface to access the count and follows good encapsulation principles by providing a controlled way to access the data.
        return Vehicle.number_of_vehicles

class Car(Vehicle): #Because Vehicles is a parameter, that means Vehicles is the superclass? Yes, when you put a class name in (), it means this class inherits from the class in (). Vehicles is the superclass, Car is the subclass.
    
    def __init__(self): #Here by default
        super().__init__() #This means we are calling Vehicle's init method and adding 1 to the number_of_vehicles

class Truck(Vehicle): #Because Vehicles is a parameter, that means Vehicles is the superclass?
     
    def __init__(self): #Here by default
        super().__init__() #This means we are calling Vehicle's init method and adding 1 to the number_of_vehicles

class Boat(Vehicle): #Because Vehicles is a parameter, that means Vehicles is the superclass?
    
    def __init__(self): #Here by default
        super().__init__() #This means we are calling Vehicle's init method and adding 1 to the number_of_vehicles

print(Car.vehicles())     # 0
car1 = Car()
print(Car.vehicles())     # 1
car2 = Car()
car3 = Car()
car4 = Car()
print(Car.vehicles())     # 4
truck1 = Truck()
truck2 = Truck()
print(Truck.vehicles())   # 6
boat1 = Boat()
boat2 = Boat()
print(Boat.vehicles())    # 8
