# What do you expect to happen when the greeting variable is referenced in the last line of the code below?

if False:
    greeting = "hello world"

print(greeting)

#If we run this as is, we get a NameError: name "greeting" is not defined. This is due to the if statement having the boolean False; because of this, greeting is never executed and initialized.
#If the if statement had the boolean True, the block will execute and greeting would initialize; we would then be able to print the object referenced by the greeting variable "hello world".
#Reminder that any if statements do not have their own scope, so if the if statement had True, greeting would be a global variable.