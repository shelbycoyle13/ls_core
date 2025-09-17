class Car:

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

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

crv = Car("Honda CRV", 2016, "silver")
crv.turn_on()
crv.accelerate(20)    
crv.show_current_speed()    
crv.accelerate(30)  
crv.show_current_speed()   
crv.brake(15)     
crv.show_current_speed()   
crv.brake(30)     
crv.show_current_speed()   
crv.turn_off()       
crv.show_current_speed()