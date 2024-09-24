# Given the following similar sets of code, what will each code snippet print?

# A
# def mess_with_vars(one, two, three):    
#     one = two       #["two"]            # The VALUES of the global variables get copied into here, but are then reassigned
#     two = three     #["three"]
#     three = one     #["two"]            #I don't see a return or print statement! <- This doesn't matter in this case, a function call 
#                                         # can still change the value of a local variable

# one = ["one"]
# two = ["two"]
# three = ["three"]

# mess_with_vars(one, two, three)           #Function is called using the global variables, the global variables get passed into the function

# print(f"one is: {one}")     #["one"]
# print(f"two is: {two}")     #["two"]
# print(f"three is: {three}") #["three"]

#Answer: Since variables one, two, and three in the mess_with_vars function are local, reassigning them does not affect the original lists. After the function finishes executing, it discards the local variables and the global variables remain unchanged.

# # B
# def mess_with_vars(one, two, three):
#     one = ["two"]
#     two = ["three"]
#     three = ["one"]                         # No return or print statement < This doesn't matter, same reason as above.
#                                 # Since it looks like there was reassignment and no mutation, global variables should be unaffected.
# one = ["one"]
# two = ["two"]
# three = ["three"]

# mess_with_vars(one, two, three)               # Function is called using the global variables, global vars get passed into the function

# print(f"one is: {one}")                 #["one"]
# print(f"two is: {two}")                 #["two"]
# print(f"three is: {three}")             #["three"]

# # Answer: The local variables inside the function are being reassigned; this has no change on the original lists.


# C
def mess_with_vars(one, two, three):
    one[0] = "two"                     # Here we actually see a reference being made to the original list; any changes will 
                                        # affect the global vars
    two[0] = "three"
    three[0] = "one"                    # No return or print statement <- This doesn't matter, same reason as above

one = ["one"]                           # Global vars
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)         # We call the function passing the global vars

print(f"one is: {one}")          #["two"]
print(f"two is: {two}")          #["three"]
print(f"three is: {three}")      #["one"]

# Answer: The function modifies the content of the lists directly. Since lists in Python are mutable and passed by reference, the changes are reflected outside the function. 
# We are modifying the contents of the lists that both the local and global variables refer to through the INDEXING we are doing. Since lists are mutable, any modification inside the function will be reflected globally.
# Overall, modifying the contents of mutable objects allows the local variables to affect global variables.
