# Write a function that takes a string and returns a dictionary containing the following three properties:

# the percentage of characters in the string that are lowercase letters
# the percentage of characters that are uppercase letters
# the percentage of characters that are neither
# All three percentages should be returned as strings whose numeric values lie between "0.00" and "100.00", respectively. Each value should be rounded to two decimal points.

# You may assume that the string will always contain at least one character.

# expected_result = {
#     'lowercase': "50.00",
#     'uppercase': "10.00",
#     'neither': "40.00",
# }
# print(letter_percentages('abCdef 123') == expected_result)

# expected_result = {
#     'lowercase': "37.50",
#     'uppercase': "37.50",
#     'neither': "25.00",
# }
# print(letter_percentages('AbCd +Ef') == expected_result)

# expected_result = {
#     'lowercase': "0.00",
#     'uppercase': "0.00",
#     'neither': "100.00",
# }
# print(letter_percentages('123') == expected_result)

"""
P
input = string
output = a dictionary (that has percentages regarding lowercase, uppercase, and neither characters)
explicit = all percentages are rounded to 2 decimal points. the string will always have at least one character
implicit = 

E
# expected_result = {
#     'lowercase': "53.85",
#     'uppercase': "7.69",
#     'neither': "38.46",
# }
# print(letter_percentages('Stitch is 626') == expected_result)


D
string
dictionary
loop

A
-initialize a dictionary with variables for lower, upper, and neither at 0
-calculate the length of the string, set that to a variable
-loop through the string:
    -if the char is lowercase
        add 1 to the count of lowercase characters
    -elif the char is uppercase
        add 1 to the count of uppercase characters
    -else:
        add 1 to the count of neither
-for the values in the dict:
    -divide all variables by the total length of the string. multiply by 100, round to 2 decimal places
    -coerce this value into a string
-return the dict

C
"""

def letter_percentages(string):

    expected_result = {
        'lowercase': 0,
        'uppercase': 0,
        'neither': 0
    }

    length_of_string = len(string)

    for char in string:
        if char.islower():
            expected_result["lowercase"] += 1
        elif char.isupper():
            expected_result["uppercase"] += 1
        else:
            expected_result["neither"] += 1
    
    for key in expected_result:
        expected_result[key] = f"{(expected_result[key] / length_of_string) * 100:.2f}"

    return expected_result

# expected_result = {
#     'lowercase': "50.00",
#     'uppercase': "10.00",
#     'neither': "40.00",
# }
# print(letter_percentages('abCdef 123') == expected_result)

# expected_result = {
#     'lowercase': "37.50",
#     'uppercase': "37.50",
#     'neither': "25.00",
# }
# print(letter_percentages('AbCd +Ef') == expected_result)

# expected_result = {
#     'lowercase': "0.00",
#     'uppercase': "0.00",
#     'neither': "100.00",
# }
# print(letter_percentages('123') == expected_result)

expected_result = {
    'lowercase': "53.85",
    'uppercase': "7.69",
    'neither': "38.46",
}
print(letter_percentages('Stitch is 626') == expected_result)

#Second, possibly more readable answer:

def letter_percentages(string):

    lowercase_total = 0
    uppercase_total = 0
    neither_total = 0

    for char in string:
        if char.islower():
            lowercase_total += 1
        elif char.isupper():
            uppercase_total += 1
        else:
            neither_total += 1
        
    lowercase_perc = lowercase_total / len(string) * 100
    uppercase_perc = uppercase_total / len(string) * 100
    neither_perc = neither_total / len(string) * 100

    char_dict = {
        'lowercase': f"{lowercase_perc:.2f}",
        'uppercase': f"{uppercase_perc:.2f}",
        'neither': f"{neither_perc:.2f}",
        }
    
    return char_dict