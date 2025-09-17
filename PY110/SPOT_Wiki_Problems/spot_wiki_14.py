# 14. Dubstep
# Write a function to decode a dubstep string to its original form.The string
# may begin and end with one or more "WUB"s and there will be at least one (and
# possibly more) "WUB"s between each word.
# The input consists of a single non-empty string, consisting only of uppercase
# English letters.

# Examples:
# song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB") # should return "WE ARE THE CHAMPIONS MY FRIEND"

"""
P
input = a string
output = a string
explicit = we want to return the original string, minus the "WUB"s
implicit = 

E

D
strings

A
-split original string by "WUB", this value is assigned to a list
-initialize a new string
-for substring in list
    -if substring == ""
        -continue
    -else:
        new_string += substring + " "
    
    return new string[:-1]

C
"""
def song_decoder(string):
    split_string = string.split("WUB")
    final_string = ""

    for substring in split_string:
        if substring == "":
            continue
        else:
            final_string += substring + " "

    return final_string[:-1]

print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB") == "WE ARE THE CHAMPIONS MY FRIEND")