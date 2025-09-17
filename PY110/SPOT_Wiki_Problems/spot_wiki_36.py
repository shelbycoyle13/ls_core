# 36. Largest Product in a series
# Complete the greatest_product method so that it'll find the greatest product of five consecutive digits in the given string of digits.

#print(greatest_product("123834539327238239583") == 3240)
#print(greatest_product("395831238345393272382") == 3240)
#print(greatest_product("92494737828244222221111111532909999") == 5292)
#print(greatest_product("92494737828244222221111111532909999") == 5292)
#print(greatest_product("02494037820244202221011110532909999") == 0)

"""
P
input = a string (of integers)
output = an integer
explicit = we want to return the largest product of 5 consecutive integers
implicit = it's possible the largest product is 0

E

D
string

A
largest_product = 1
current_product = 1
count = 0

iterate through the string, for i, digit in enumerate(string)
    current_product *= int(digit)
    count += 1
    if count == 5
        count = 0
        if current_product >= largest_product:
            largest_product = current_product

return largest_product

C
"""
def greatest_product(string):
    largest_product = 0

    for i in range(len(string) - 4): #Easiest way to remember this format is if you want a window of length 5, subtract 1 less
        current_window = string[i: i + 5] #Slicing stop number is non-inclusive, so can add exactly the amount you need
        current_product = 1

        for digit in current_window: #We're only iterating over the 5 numbers at hand. We had to nest this in the for loop that is able to construct the window
            current_product *= int(digit)

        if current_product > largest_product:
            largest_product = current_product

    return largest_product

print(greatest_product("123834539327238239583") == 3240)
print(greatest_product("395831238345393272382") == 3240)
print(greatest_product("92494737828244222221111111532909999") == 5292)
print(greatest_product("92494737828244222221111111532909999") == 5292)
print(greatest_product("02494037820244202221011110532909999") == 0)