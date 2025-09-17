# Given an instance of a Foo object, show two ways to print I am a Foo object without hardcoding the word Foo.

class Foo:

    pass

thing = Foo()

print(f"I am a {thing.__class__.__name__} object")