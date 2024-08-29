# Build a program that displays when the user will retire and how many years she has to work till retirement.

import datetime

age = int(input("What is your age? "))
goal_age = int(input("At what age would you like to retire? "))
years_to_goal = goal_age - age

time = datetime.datetime.now()
year = int(time.strftime("%Y"))


print(f"It's {year}. You will retire in {year + years_to_goal}.")
print(f"You have only {years_to_goal} years of work to go!")