# How can you determine whether a given string ends with an exclamation mark (!)? Write some code that prints True or False depending on whether the string ends with an exclamation mark.

str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

def check_syntax(string):
    if string.endswith("!"):
        print("True")
    else:
        print("False")

check_syntax(str1)
check_syntax(str2)

#My solution is the function definition called check_syntax() and I've called it twice with the two string arguments on lines 12 and 13.