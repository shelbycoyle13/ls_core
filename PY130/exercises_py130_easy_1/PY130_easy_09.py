# Basic Generator Function
# Create a generator function that yields numbers from 1 to 5.

def give_number():
    for num in range(1, 6):
        yield num

for num in give_number():
    print(num)