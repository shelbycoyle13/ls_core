# 4. Print the method resolution order for cars, trucks, boats, and vehicles as defined in the previous exercise.

class SignalMixin: #We type mix-ins like we would a class
                            #By convention, mix-ins typically do not have an init method.
    def signal_left(self):
        print("Signalling left")

    def signal_right(self):
        print("Signalling right")

    def signal_off(self):
        print("Signal is now off")

class Vehicle:
    number_of_vehicles = 0

    def __init__(self): 
        Vehicle.number_of_vehicles += 1 

    @classmethod
    def vehicles(cls):
        return Vehicle.number_of_vehicles

class Car(SignalMixin, Vehicle): #We only want to use the mix-in with Car and Truck. The mix-in is the first parameter. Putting mix-ins first is convention. Also worth mentioning is the MRO, which means that by putting the mix-in first, it will search for methods there first before Vehicle. 
    
    def __init__(self):
        super().__init__() 

class Truck(SignalMixin, Vehicle): #We only want to use the mix-in with Car and Truck. The mix-in is the first parameter.
     
    def __init__(self): 
        super().__init__() 

class Boat(Vehicle):
    
    def __init__(self): 
        super().__init__() 


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
car1.signal_left()       # Signalling left #If it looks like a method, it's written like a function definition above
truck1.signal_right()    # Signalling right
car1.signal_off()        # Signal is now off
truck1.signal_off()      # Signal is now off
# boat1.signal_left()
# AttributeError: 'Boat' object has no attribute
# 'signal_left'

print(Car.mro())
print(Truck.mro())
print(Boat.mro())
print(Vehicle.mro())