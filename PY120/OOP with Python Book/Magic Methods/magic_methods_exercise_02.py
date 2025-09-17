# 2. Don't let the mathiness of this problem scare you off. You don't have to know any math; you only need to know how to write code.

# Earlier, we wrote the following class:
    
#     class Vector:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplemented

#         new_x = self.x + other.x
#         new_y = self.y + other.y
#         return Vector(new_x, new_y)

#     # __iadd__ method omitted; we don't need it for this exercise

#     def __repr__(self):
#         x = repr(self.x)
#         y = repr(self.y)
#         return f'Vector({x}, {y})'

# v1 = Vector(5, 12)
# v2 = Vector(13, -4)
# print(v1 + v2)      # Vector(18, 8)

# Update this class so the following code works as indicated:

# print(v1 - v2) # Vector(-8, 16)
# print(v1 * v2) # 17
# print(abs(v1)) # 13.0

# In this code, the * operator should compute the dot product of the two vectors. For instance, if you have Vector(a, b) and Vector(c, d), the dot product is a * c + b * d, where * and + are the usual arithmetic operators.

# The abs function computes the magnitude of a vector. If you have a vector Vector(a, b), the magnitude is given by sqrt(a**2 + b**2). You will need the math module to access the sqrt function. Note that abs is a built-in function, so you don't want to override it entirely; you only want to change its behavior for Vector objects. There's a magic method you can use.

# Don't worry about augmented assignment in this exercise.
import math

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    # __iadd__ method omitted; we don't need it for this exercise

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)
    
    def __mul__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        new_x = self.x * other.x
        new_y = self.y * other.y

        dot_product = new_x + new_y
        return dot_product

    def __abs__(self):
        sum_of_squares = ((self.x**2) + (self.y**2))

        return math.sqrt(sum_of_squares)

    def __repr__(self):
        x = repr(self.x)
        y = repr(self.y)
        return f'Vector({x}, {y})'

v1 = Vector(5, 12)
v2 = Vector(13, -4)
print(v1 + v2)      # Vector(18, 8)

print(v1 - v2) # Vector(-8, 16)
print(v1 * v2) # 17 # We want to return the dot product here
print(abs(v1)) # 13.0