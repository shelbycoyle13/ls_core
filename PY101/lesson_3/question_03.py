# Starting with the string below:

# Show two different ways to create a new string with "Four score and " prepended to the front of the string.

famous_words = "seven years ago..."

def prepend_words(string):                      
    new_string = "Four score and " + string
    return new_string

print(prepend_words(famous_words))

#My first option used concatenation. I created a function definition called prepend_words() with a parameter of string. Inside of the function body, I initialized a new variable called new_string which is assigned to the concatenation of the string "Four score and " and the string variable. Then I return the new string. Calling the function with the famous_words argument prints out the string we want.

def prepend_words(string):
    print(f"Four score and {famous_words}")

prepend_words(famous_words)

#The second option is to simply print an f-string. This doesn't need to be in a function, but to make it similar to the previous answer, I left the print statement inside the same function name.