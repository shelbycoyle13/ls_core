# Start the Engine (Part 1)
# Change the following code so that creating a new Truck automatically calls start_engine.

class Vehicle:
    def __init__(self, year):
        self._year = year

    @property
    def year(self):
        return self._year

class Truck(Vehicle):
    def __init__(self, year):
        super().__init__(year) #The super function allows us to call methods from the parent class. We call the initializer and want to pass in the year argument.
        self.start_engine()

    def start_engine(self):
        print('Ready to go!')

# Comments show expected output
truck1 = Truck(1994)          # Ready to go!
print(truck1.year)            # 1994