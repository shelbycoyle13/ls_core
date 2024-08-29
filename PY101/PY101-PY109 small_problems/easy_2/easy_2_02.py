# Write a program that asks for user's name, then greets the user. If the user appends a ! to their name, the computer will yell the greeting (print it using all uppercase).

user_input = input("What is your name? ")

if user_input.endswith("!"):
    print((f'Hello {user_input} Why are we yelling?').upper())
else:
    print(f'Hello {user_input}.')