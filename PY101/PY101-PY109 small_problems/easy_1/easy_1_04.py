# Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

# length = abs(float(input("Please enter the length of the room in meters: ")))
# width = abs(float(input("Please enter the width of the room in meters: ")))

# def calculate_area(length, width):
#     area_meters = length * width
#     area_feet = area_meters * 10.7639

#     print(f"This room's area is {area_meters} in square meters and {area_feet} in square feet.")

# calculate_area(length, width)

# Further Exploration
# Modify the program to let the user specify the measurement type (meters or feet). Compute the area accordingly and print it and its conversion in parentheses.

def calculate_area_meters(length, width):
    area_meters = length * width
    print(f"This room's area is {area_meters} in square meters.")

def calculate_area_feet(length, width):
    area_feet = length * width
    print(f"This room's area is {area_feet} in square feet.")

preference = input("For measurements, do you prefer meters or feet? ")

def area_choice(preference):
    if preference == "meters":
        length = abs(float(input("Please enter the length of the room: ")))
        width = abs(float(input("Please enter the width of the room: ")))
        calculate_area_meters(length, width)
    elif preference == "feet":
        length = abs(float(input("Please enter the length of the room: ")))
        width = abs(float(input("Please enter the width of the room: ")))
        calculate_area_feet(length, width)
    else:
        print("You must've entered an invalid response. Please run this again.")

area_choice(preference)