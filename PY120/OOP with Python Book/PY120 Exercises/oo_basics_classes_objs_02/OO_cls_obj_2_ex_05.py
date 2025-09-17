# Counting Cats
# Create a class named Cat that tracks the number of times a new Cat object is instantiated. The total number of Cat instances should be printed when total is invoked.

class Cat:
    total_cats = 0 #This is a class variable

    def __init__(self):
        Cat.total_cats += 1 #Here we would say, the Cat class accesses its total_cats variable. When we use the syntax Cat.number_of_cats, we're telling Python "go to the Cat class and get me the value stored in the number_of_cats variable.

    @classmethod
    def total(cls):
        print(cls.total_cats)

Cat.total()         # 0

kitty1 = Cat()
Cat.total()         # 1

kitty2 = Cat()
Cat.total()         # 2

print(Cat())        # <__main__.Cat object at 0x104ed7290>
Cat.total()         # 3