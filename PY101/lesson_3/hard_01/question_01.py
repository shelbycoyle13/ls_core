# Will the following functions return the same results? Try to answer without running the code or looking at the solution.

def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first()) # {"prop1" : "hi there"}
print(second()) # Indentation error? or None

# The second function returns None. This is because there is nothing immediately after return on the same line.
# No error is thrown; but the code that comes on the lines under the return statement become unreachable.
# Remember, after a return statement, the function terminates!

# def example_function():
#     print("This will print.")
#     return "Returning from the function."     # Function doesn't execute past this point!
#     print("This will NOT print.")

# result = example_function()                   # Function call executes on the right hand side first. It prints the output AND assigns 
#                                                 the return value to result
# print(result)  # Outputs: Returning from the function.
