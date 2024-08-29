# Write a function that takes two arguments, a string and a positive integer, then prints the string as many times as the integer indicates.

def repeat(string, integer):
    for i in range(0, integer):
        print(string)

repeat('Hello', 3)

