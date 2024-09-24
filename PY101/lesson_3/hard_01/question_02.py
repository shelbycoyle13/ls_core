# What does the last line in the following code output?

dictionary = {'first': [1]}     # We initialize dictionary and assign it a dictionary
num_list = dictionary['first']  #[1]    - We initialize num_list to the value of the key
num_list.append(2)              #[1, 2] - This line of code is mutating, it mutates the value of the key in dictionary

print(num_list)                 #[1, 2]
print(dictionary)               #{'first': [1, 2]}

# Try to answer without running the code or looking at the solution.

# Because num_list is a REFERENCE to the ORIGINAL list in dictionary, appending to num_list modifies the list in the original dictionary.
# MUTABLE OBJECTS SUCH AS DICTIONARIES (or lists) ARE NOT COPIED WHEN ASSIGNED TO A NEW VARIABLE - THEY ARE REFERENCED!

# If we only wanted to modify my_list but not the original dictionary, there are two ways we could do this:

# Initialize num_list with a reference to a COPY of the original dictionary:
# dictionary = {"first": [1]}
# num_list = dictionary["first"].copy()
# num_list.append(2)

# We can use slicing which returns a new list:
# dictionary = {"first": [1]}
# num_list = dictionary["first"][:]
# num_list.append(2)