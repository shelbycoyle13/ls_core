# 11. Extract the domain name from a URL

# Write a function that, given a URL as a string, parses out just the domain
# name and returns it.

# Examples:
# domain_name("http://github.com/carbonfive/raygun") # should return "github"
# domain_name("https://www.cnet.com") # should return "cnet"

"""
P
input = a string
output = a string
explicit = we just want to return the domain name from the original string (i.e. the string right before .com)
implicit = sometimes the string has www and sometimes it doesnt. but it looks like both test cases have //

E

D
string
list

A
high level:
-split the string by //
-split again by .com
-just return the string after the non-alpha characters and before the .com

C
"""

def domain_name(string):
    first_split = string.split("//") #Remember that whatever you are splitting by doesn't appear in the list anymore
    second_split = []
    for substring in first_split:
        second_split.append(substring.split(".com"))

    if second_split[1][0].startswith("www."):
        return second_split[1][0][4:]
    
    return second_split[1][0]           

print(domain_name("http://github.com/carbonfive/raygun")) # should return "github"
print(domain_name("https://www.cnet.com")) # should return "cnet"