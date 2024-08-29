user_input_int = input("Please enter integers greater than 0: ")

def get_valid_integers(user_input_int):
    user_input_int = input("Please enter integers greater than 0: ")
    split_input = user_input_int.split(" ")
    list_of_integers = []
    
    for integer in split_input:
        while not integer.isdigit() or int(integer) <= 0:
            print("You didn't enter valid integers. Please start over.")
            user_input_int = input("Please enter integers greater than 0: ")
        list_of_integers.append(int(integer))

def get_valid_preference(preference):  
    preference = input("Enter 's' to compute the sum, or 'p' to compute the product. ")  
    if preference != "s" or "p":
        print("You didn't input the correct letter, so this is an error.")

get_valid_integers(user_input_int)
get_valid_preference(preference)