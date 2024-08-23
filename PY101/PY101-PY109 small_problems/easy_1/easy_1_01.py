# # Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.

# def is_it_odd(int):
#     if abs(int) % 2 != 0:
#         return True
#     else:
#         return False
    
# print(is_it_odd(-2))

def is_odd(number):
    return number % -3

print(is_odd(-4))