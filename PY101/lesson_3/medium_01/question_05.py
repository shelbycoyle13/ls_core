# What do you think the following code will output?

nan_value = float("nan")

print(nan_value == float("nan")) #I think this will print False, with the combination of a float and nan, this doesn't seem to make sense

# Answer: nan = "not a number" - this is a special numeric value that indicates that an operation that was intended to return a number has failed. Python does not let you use == to determine whether a number is nan!

# Bonus Question

# How can you reliably test if a value is nan?

import math

print(math.isnan(nan_value))