# Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive.
# Example 1:
# Please enter an integer greater than 0: 5
# Enter "s" to compute the sum, or "p" to compute the product. s

# The sum of the integers between 1 and 5 is 15.

# Example 2:
# Please enter an integer greater than 0: 6
# Enter "s" to compute the sum, or "p" to compute the product. p

# The product of the integers between 1 and 6 is 720.

# integer = abs(int(input("Please enter an integer greater than 0: ")))
# preference = input("Enter 's' to compute the sum, or 'p' to compute the product. ")

# def sum_or_product(integer):
#     if preference == 's':
#         sum = 0
#         for i in range(1, integer + 1):
#             sum += i
#         print(sum)
#     elif preference == 'p':
#         product = 1
#         for i in range (1, integer + 1):
#             product *= i
#         print(product)
#     else:
#         print("You didn't input the correct values, so this is an error.")

# sum_or_product(integer)

# Further Exploration
# Suppose the input was a list of space separated integers instead of just a single integer? How would your compute_sum and compute_product functions change?

user_input_int = input("Please enter integers greater than 0: ")
split_input = user_input_int.split(" ")
list_of_integers = []


for integer in split_input:
    while True:
        try:
            if integer.isdigit() or int(integer) > 0:
                list_of_integers.append(int(integer))
                break
            else:
                print("You didn't enter valid integers. Please start over.")
                user_input_int = input("Please enter integers greater than 0: ")
        except ValueError:
            print("Testing testing")
        
# preference = input("Enter 's' to compute the sum, or 'p' to compute the product. ")
    
# if preference != "s" or "p":
#     print("You didn't input the correct letter, so this is an error.")

# def sum_or_product():
#     if preference == 's':
#         total_sum = 0
#         for i in get_valid_input:
#             total_sum += i
#         return total_sum
#     elif preference == 'p':
#         total_product = 1
#         for i in get_valid_input:
#             total_product *= i
#         return total_product
#     else:
#         print("Something went wrong.")
        

# sum_or_product(get_valid_int, get_valid_preference)