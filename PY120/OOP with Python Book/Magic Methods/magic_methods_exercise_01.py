# 1. Create a Car class that makes the following code work as indicated:

# vwbuzz = Car('ID.Buzz', 2024, 'red')
# print(vwbuzz)        # Red 2024 ID.Buzz
# print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')

class Car:

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        return f"{self.color.title()} {self.year} {self.model.title()}"

    def __repr__(self):
        return f"Car({repr(self.model)}, {repr(self.year)}, {repr(self.color)})"

vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')