# Generic Greeting (Part 1)
# Create a class named Cat for which calling Cat.generic_greeting prints Hello! I'm a cat!.

# class Cat:
#     @classmethod
#     def generic_greeting(cls):
#         print("Hello! I'm a cat!")

# Cat.generic_greeting() #Hello! I'm a cat! #Note that the class itself is calling this method, hence why we're decorating this with a @classmethod.

# Further Exploration
# What happens if you run type(kitty).generic_greeting()? Can you explain this result?

class Cat:
    @classmethod
    def generic_greeting(cls):
        print("Hello! I'm a cat!")

kitty = Cat()
kitty.generic_greeting()      # Hello! I'm a cat!

type(kitty).generic_greeting() #To answer the previous question, this line also prints "Hello! I'm a cat!" I think this is because the caller of the method is the result of type(kitty), which is essentially still part of the Cat class type. Because it's part of Cat, it is able to print the same result.