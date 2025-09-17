# Rectangles and Squares
# Given the class from the previous problem:

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width * self._height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side) # Can you please tell me the process of what's taking place in this line? I understand super inherits from the superclass but the rest of the syntax confuses me a bit
    
# Write a class called Square that inherits from the Rectangle class. The Square class is used like this:

square = Square(5)
print(square.area == 25)      # True