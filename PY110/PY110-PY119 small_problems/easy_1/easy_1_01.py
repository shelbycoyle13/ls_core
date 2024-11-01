# Searching 101

# Write a program that solicits six (6) numbers from the user and prints a message that describes whether the sixth number appears among the first five.

# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 17

# 17 is in 25,15,20,17,23.

# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 18

# 18 isn't in 25,15,20,17,23.

# P
# input = integers from the user
# output = string including integers from the user
# explicit rules = we are utilizing user input. outputs a string. is the 6th integer inputted already appear in the previous 5 integers given?
# implicit = user input is a string

# E
# Examples are above

# D
# List, strings

# A 
# - We first need to set up a prompt to ask the user to enter integers
# - We need to make sure the prompt appears 6 times - notice they are all different prompts!
# - User enters 6 integers
# - We need to convert the strings to integers
# - Add the integers to a list
# - Check if the 6th integer has membership in the list
# - Output the result of the membership

# C
integers_list = []

user_prompt = int(input("Enter the 1st number: "))
integers_list.append(user_prompt)
user_prompt = int(input("Enter the 2nd number: "))
integers_list.append(user_prompt)
user_prompt = int(input("Enter the 3rd number: "))
integers_list.append(user_prompt)
user_prompt = int(input("Enter the 4th number: "))
integers_list.append(user_prompt)
user_prompt = int(input("Enter the 5th number: "))
integers_list.append(user_prompt)
user_prompt6 = int(input("Enter the last number: "))
integers_list.append(user_prompt6)

if user_prompt6 in integers_list[:5]:
    print(f"{user_prompt6} is in {', '.join(map(str, integers_list[:5]))}")
else:
    print(f"{user_prompt6} isn't in {', '.join(map(str, integers_list[:5]))}")

# Further Exploration
# Suppose we alter the problem to look for a number that satisfies a condition (e.g., a number greater than 25) instead of a specific number? Would the current solution still work? Why or why not?

for number in integers_list:
    if number > 25:
        print(f"Cool, {number} is greater than 25!")

# My solution already had changed the input to integers; while the current code I had didn't compare numbers, it wasn't difficult to add another piece of code to do so.