# What will the following two lines of code output?

# print(0.3 + 0.6) #0.9
# print(0.3 + 0.6 == 0.9) # 0.9 == 0.9 -> True

# My prediction was incorrect. The correct outputs are:
# 0.8999999999999999
# False

# Why is this? This is because Python uses floating point numbers for all numeric operations. Most floating point represenations used on computers lack a certain amount of precision, leading to the result we see here. 
# This solution below with the .isclose method is better to use.

import math

print(0.3 + 0.6)
print(math.isclose(0.3 + 0.6, 0.9))