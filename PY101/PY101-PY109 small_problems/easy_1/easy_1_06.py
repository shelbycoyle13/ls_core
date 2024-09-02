# Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive.

# Suppose the input was a list of space separated integers instead of just a single integer? How would your compute_sum and compute_product functions change?

def compute_sum(numbers):
    return sum(numbers)

def compute_product(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

while True:
    user_input = input("Please enter integers greater than 0, separated by spaces: ")

    try:
        user_integers = [int(chr) for chr in user_input.split() if int(chr) > 0]
        if not user_integers:
            raise ValueError("No valid integers were entered.") 
    except ValueError:
        print("Invalid input. Please enter only integers greater than 0.")
    else:
        break

while True:
    user_preference = input('Enter "s" to compute the sum, or "p" to compute the product. ')

    if user_preference == "s":
        print(f"The sum of the integers {user_integers} is {compute_sum(user_integers)}.")
        break
    elif user_preference == "p":
        print(f"The product of the integers {user_integers} is {compute_product(user_integers)}.")
        break
    else:
        print("Sorry, you did not choose a valid letter. Please try again.")

    
# Please enter an integer greater than 0: 5
# Enter "s" to compute the sum, or "p" to compute the product. s

# The sum of the integers between 1 and 5 is 15.


# Please enter an integer greater than 0: 6
# Enter "s" to compute the sum, or "p" to compute the product. p

# The product of the integers between 1 and 6 is 720.