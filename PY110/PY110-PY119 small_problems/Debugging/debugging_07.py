# We defined a function intending to multiply the sum of numbers by a factor. However, the function raises an error. Why? How would you fix this code?

# def sum(numbers, factor):
#     return factor * sum(numbers) # The problem lies here. We are trying to use the built in function called sum but we also named our 
                                    # own function called sum. This led to shadowing the built-in function.

# numbers = [1, 2, 3, 4]
# print(sum(numbers, 2) == 20)

def sum_then_multiply(numbers, factor): # Simply renaming our function will fix this problem.
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum_then_multiply(numbers, 2) == 20)