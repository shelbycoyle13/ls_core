class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.sides = [side1, side2, side3]

        if not all(side > 0 for side in self.sides):
            raise ValueError("Sides must be greater than 0")
        
        a, b, c = sorted(self.sides)
        if a + b <= c:
            raise ValueError("Invalid triangle")

    @property
    def kind(self):
        if self.side1 == self.side2 == self.side3:
            return 'equilateral'
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return 'isosceles'
        else:
            return 'scalene'
