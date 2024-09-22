# Alan wrote the following function, which was intended to return all of the factors of number:

def factors(number):
    if number > 0:
        divisor = number
    else:
        return "Sorry, we don't accept negative numbers"
    result = []
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

# Alyssa noticed that this code would fail when the input is a negative number, and asked Alan to change the loop. How can he make this work? Note that we're not looking to find the factors for negative numbers, but we want to handle it gracefully instead of going into an infinite loop.

# I added an if statement in the first line of the function body, so as to filter out negative numbers from going into the while loop to begin with. I also added a string to indicate that we don't accept negative numbers.

# This line of code in the while loop is also an acceptable answer:
# while divisor > 0:

# Bonus Question: What is the purpose of number % divisor == 0 in that code?

# We want to make sure that the number divided by the divisor has a result with no remainder. This will ensure that the integers that are being added to our result list are whole numbers, not floats, and therefore are actual factors of the number passed as the argument.

print(factors(-9))
print(factors(9))