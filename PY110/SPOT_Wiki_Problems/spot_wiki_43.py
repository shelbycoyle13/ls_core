# 43. Digit Power Play
# Some numbers have funny properties. For example:
# 89 --> 8¹ + 9² = 89 * 1
# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
# Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n.
# In other words:
# Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
# If it is the case, we will return k; if not return -1.
# Note: n and p will always be given as strictly positive integers.

#print(dig_pow(89, 1) == 1)
#print(dig_pow(92, 1) == -1)
#print(dig_pow(46288, 3) == 51)
#print(dig_pow(695, 2) == 2)

"""
P
input = two integers
output = one integer
explicit = first we have our given number, followed by a given power. we separate each digit and then raise them to the power, starting with the first power, then going up one for each digit. once we reach the end of the number, sum this. if the sum is divisible by the original number argument, return the quotient. If not possible, return -1.
implicit = 

E

D


A
-current total = 0
-coerce the first argument to a string
    -for int(digit) in string
        product = digit ** power
        add product to current total
        add 1 to the power

if current total % first argument == 0
    return current total / first argument
else
    return -1

C
"""
def dig_pow(number1, power):
    current_total = 0
    num_as_string = str(number1)

    for digit in num_as_string:
        product = int(digit) ** power
        current_total += product
        power += 1

    if current_total % number1 == 0:
        return current_total // number1
    else:
        return -1

print(dig_pow(89, 1) == 1)
print(dig_pow(92, 1) == -1)
print(dig_pow(46288, 3) == 51)
print(dig_pow(695, 2) == 2)