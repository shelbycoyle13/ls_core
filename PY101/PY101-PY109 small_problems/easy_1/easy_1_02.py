# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

# for num in range(1, 100, 2):
#     print(num)

# Consider adding a way for the user to specify the starting and ending values of the odd numbers printed.

start_num = int(input('Please enter a starting number: '))
end_num = int(input('Please enter an ending number: '))

def check_nums(start_num, end_num):
    while start_num > end_num:
        print("Your starting number must be less than the ending number for this to work.")
        start_num = int(input('Please enter a starting number: '))
        end_num = int(input('Please enter an ending number: '))
    
    for num in range(start_num, end_num + 1):
        if num % 2 != 0:
            print(num)

check_nums(start_num, end_num)