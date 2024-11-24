# Write a function that takes a string as an argument and returns True if all parentheses in the string are properly balanced, False otherwise. To be properly balanced, parentheses must occur in matching '(' and ')' pairs.

# Note that balanced pairs must start with a (, not a ).

# print(is_balanced("What (is) this?") == True)        # True
# print(is_balanced("What is) this?") == False)        # True
# print(is_balanced("What (is this?") == False)        # True
# print(is_balanced("((What) (is this))?") == True)    # True
# print(is_balanced("((What)) (is this))?") == False)  # True
# print(is_balanced("Hey!") == True)                   # True
# print(is_balanced(")Hey!(") == False)                # True
# print(is_balanced("What ((is))) up(") == False)      # True

"""
P
input = a string
output = a Boolean
explicit = "properly balanced" starts with a ( and must be in pairs
implicit = it looks like the () don't have to be balanced in a certain location in the string, we just have to have the same number of pairs

E
# print(is_balanced("(What (is for) lunch?)") == True)        # True

D
loops

A
-iterate through the string
    - use the find method to return the first index of (
    - use the find method to return the first index of )
    - if index of ) is less than (
        - return false
    - else:
        - use the count method to return the number of (
        - use the count method to return the number of )
        if the values are the same:
            if the entire number of ( appear before ) - we could try using .rfind():
                return True
        else:
            return False

C
"""
def is_balanced(string):
    for char in string:
        first_paren_index = string.find("(")
        closing_paren_index = string.find(")")
        if closing_paren_index < first_paren_index:
            return False
        else:
            count_first_paren = string.count("(")
            count_closing_paren = string.count(")")
            if (count_first_paren == count_closing_paren) and (string.rfind("(") <= string.rfind(")")):
                return True
            else:
                return False

print(is_balanced("What (is) this?") == True)        # True            
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True
print(is_balanced("(What (is for) lunch?)") == True)        # True