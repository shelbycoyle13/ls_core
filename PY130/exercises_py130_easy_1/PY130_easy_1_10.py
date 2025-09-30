# Generator with User Input
# Create a generator function that yields user input strings until the word "stop" is entered.

def give_string():
    input_list = []
    user_input = input("Please enter one word at a time. When you type 'stop' this program will end. Enter here: ")
    if user_input != "stop":
        yield user_input
    else:
        return
    
    while user_input != "stop":
        user_input = input("Please enter one word at a time. When you type 'stop' this program will end. Enter here: ")
        if user_input != "stop":
            yield user_input
            input_list.append(user_input)

    return input_list

for string in give_string():
    print(string)


#LS Solution (much more simple than mine):
# def input_generator():
#     while True:
#         s = input("Enter a string: ")
#         if s == "stop":
#             break
#         yield s

# for user_input in input_generator():
#     print(user_input)