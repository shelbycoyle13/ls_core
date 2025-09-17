class Car:

    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self._color = color
        self._speed = 0

    def turn_on(self):
        print(f"The {self.model} has been turned on!")

    def accelerate(self, number):
        self.speed += number
        print(f"We are accelerating the {self.model} by {number} miles per hour!")

    def brake(self, number):
        self.speed -= number
        print(f"We hit the brake on the {self.model}! We are decreasing the speed by {number} miles per hour!")

    def turn_off(self):
        self.speed = 0
        print(f"The {self.model} has been turned off!")

    def show_current_speed(self):
        print(f"Current speed of the {self.model} is {self.speed} miles per hour!")

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise TypeError("New color must be a string")
        self._color = color

    @property
    def model(self):
        return self._model
    
    @property
    def year(self):
        return self._year

    def spray_paint(self, color):
        self.color = color
        print(f"Your car is now painted {color}!")

    @classmethod
    def gas_mileage(cls, miles, gallons):
        mileage = miles / gallons
        print(f"This car's gas mileage is {mileage} miles per gallon.")

Car.gas_mileage(351, 13)