# Start the Engine (Part 2)
# Given the following code, modify Truck.start_engine by appending 'Drive fast, please!' to the return value of Vehicle.start_engine. The 'fast' in 'Drive fast, please!' should be taken from the value of the speed argument.

class Vehicle:
    def start_engine(self):
        return 'Ready to go!'

class Truck(Vehicle):
    def start_engine(self, speed):
        return super().start_engine() + f' Drive {speed}, please!' #We don't use double underscores because start_engine is not a magic method (and we're also trying to override this regular method)

# Comments show expected output
truck1 = Truck()
print(truck1.start_engine('fast'))
# Ready to go! Drive fast, please!

truck2 = Truck()
print(truck1.start_engine('slow'))
# Ready to go! Drive slow, please!