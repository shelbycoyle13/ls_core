# This is just a visual of what the dictionary looks like to set up the board

# board = {
#   1: 'X', # top left
#   2: ' ', # top center
#   3: ' ', # top right
#   4: ' ', # middle left
#   5: 'O', # center
#   6: ' ', # middle right
#   7: ' ', # bottom left
#   8: ' ', # bottom center
#   9: 'X',  # bottom right
# }

"""
Using PEDAC to create a helper function called join_or

    P
    input = list
    output = a string, with the last integer in the list "prepended" with or
    explicit = We always take a list, even if the list is empty. Some arguments with lists are followed by other symbols.
    implicit = If followed by a symbol, we apply after each integer. If after the symbol, we see "and" instead, we should use that instead of "or". Empty lists return empty strings. If there's two integers, there's no need for a comma. If there's three integers we use a comma.

    E
    print(join_or([1, 2, 3, 4], '; ', 'and'))  # => "1; 2; 3; and 4"
    
    D 
    lists, possibly for loops, strings

    A
    initialize an empty final string

    iterate over the list - for every integer in list, add to final string
        if the list is empty, return an empty string
        if the list only has 1 integer, add and return the finals string
        if the list has two integers, add the first integer, concatenate "or" then the final integer
        if the list has 3 or more integers
            add the integer, concatenate a comma, after the second to last integer, concatenate "or" then the final integer
            if there's an additional symbol argument, add the integer, concatenate the symbol, after the second to last integer, concatenate "or" then the final integer
                if there's an additional symbol argument and "and, add the integer, concatenate the symbol, after the second to last integer, concatenate "and" then the final integer

    return final string

    C
    """

# print(join_or([1, 2, 3]))               # => "1, 2, or 3"
# print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
# print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
# print(join_or([]))                      # => ""
# print(join_or([5]))                     # => "5"
# print(join_or([1, 2]))                  # => "1 or 2"