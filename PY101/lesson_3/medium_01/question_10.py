# In Python, every object has a unique identifier that can be accessed using the id() function. This function returns the identity of an object, which is guaranteed to be unique for the object's lifetime. For certain basic immutable data types like short strings or integers, Python might reuse the memory address for objects with the same value. This is known as "interning".

# Given the following code, predict the output:

a = 42      # Memory address 123
b = 42      # Same address 123
c = a       # Points to address 123

print(id(a) == id(b) == id(c)) #True

# When working with integers -5 to 256, memory locations are preassigned for each individual number. So 42 has its own address, 41 has it's own address, etc.

a = 1000      # Memory address 123
b = 1000      # Same address 123
c = a       # Points to address 123

print(id(a) == id(b) == id(c)) #True

# Sometimes integers above 256 can still point to the same memory address. It can reuse the objects and not make new ones, especially if they are created in the same context (in the same execution environment or session). Sometimes it depends on the Python implementation or version as well. Implementation refers to a Python variant (CPython, PyPy, Jython, etc)