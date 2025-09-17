# Find the Class
# Update the following code so that, instead of printing the values, each statement prints the name of the class to which it belongs.

# Comments show expected output

print(type("Hello"))    # <class 'str'>
print(type(5))                      # <class 'int'>
print(type([1, 2, 3]))             # <class 'list'>

#We use the type function to get the exact output with the angle brackets. I originally was thinking of using .__class__.__name__, but that only works to get "int", "str", "list", etc, but that's not the output we are looking for. Using only .__class__ is an option too to get the correct, same answer!