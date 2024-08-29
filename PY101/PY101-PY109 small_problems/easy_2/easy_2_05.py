# Write a program that prompts the user for two positive numbers (floating-point), then prints the results of the following operations on those two numbers: addition, subtraction, product, quotient, floor quotient, remainder, and power. Do not worry about validating the input. #

first = abs(float(input("Enter the first number: ")))
second = abs(float(input("Enter the second number: ")))

def results(first, second):
    print(f'{first} + {second} = {first + second}')
    print(f'{first} - {second} = {first - second}')
    print(f'{first} * {second} = {first * second}')
    print(f'{first} / {second} = {first / second}')
    print(f'{first} // {second} = {first // second}')
    print(f'{first} % {second} = {first % second}')
    print(f'{first} ** {second} = {first ** second}')
         
results(first, second)