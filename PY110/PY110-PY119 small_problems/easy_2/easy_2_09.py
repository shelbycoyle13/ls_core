# How Many?
# Write a function that counts the number of occurrences of each element in a given list. Once counted, print each element alongside the number of occurrences. Consider the words case sensitive e.g. ("suv" != "SUV").

# vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
#             'motorcycle', 'motorcycle', 'car', 'truck']

# count_occurrences(vehicles)

# # your output sequence may appear in a different sequence
# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2

# P
# input = list
# output = strings
# explicit = we need to count each elemenent in a list. this is case-sensitive. 
# implicit = 

# E
# colors = ["red", "orange", "pink", "red", "yellow", "yellow"]
# red => 2
# orange => 1
# pink => 1
# yellow => 2


# D
# lists, for loops, dictionary

# A
# we need to iterate through the list
# for every element, set a count of each occurrence 
# when the loop is finished, print the element and its count

# C

def count_occurrences(lst):
    new_dict = {}

    for element in lst:
        count = lst.count(element)
        new_dict[element] = count
    for key, value in new_dict.items():
        print(f"{key} => {value}")

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

colors = ["red", "orange", "pink", "red", "yellow", "yellow"]

count_occurrences(colors)