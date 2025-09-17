# It is quite common to find yourself in a situation where you need to perform a search on some data to find something you're looking for. Imagine that you need to search through an old-fashioned phone book. Back in the day, phone books were printed every year by phone companies. The phone books contained an alphabetical list (by last name) of every customer, together with their phone number. A straightforward way to search the phone book would be to go through the phone book one name at a time, checking whether the current name is the one you're trying to find.

# This may be a simple and easy way to search, but it's not very efficient. In the worst case scenario, it could mean having to search through every single name in the book, and some phone books could be over 1000 pages. A linear search such as this can take quite a long time.

# A binary search is a much more efficient alternative. This algorithm lets you cut the search area in half on each iteration by discarding the half that you know your search term doesn't exist in. The binary search algorithm is able to do this by relying on the data being sorted. Going back to the phone book example, let's say that we're searching the following phone_book data for the search item 'Smith':

# Phone book data
# phone_book = [
#     'Embry',
#     'Hanson',
#     'Hawkins',
#     'John',
#     'Lee',
#     'Seeli',
#     'Smith',
#     'Zimmer',
# ]

# With a linear search, we would have to sequentially go through each of the names until we found the search item, 'Smith'. In a binary search, however, the following sequence happens:

# Retrieve the middle value from the data (assume truncation to integer) --> 'John'.
# If the middle value is equal to 'Smith', stop the search.
# If the middle value is less than 'Smith':
# Discard the lower half, including the middle value --> `['Embry', 'Hanson', 'Hawkins', 'John'].
# Repeat the process from the top, using the upper half as the starting data --> ['Lee', 'Seeli', 'Smith', 'Zimmer'].
# If the middle value is greater than 'Smith', do the same as the previous step, but with opposite halves.
# Using the process described above, the search successfully ends on the third iteration when the middle value is 'Smith'. For an 8-element list like this, we need, at most, 3 iterations. For an 8000-element list, we need, at most, just 13 iterations. For 8,000,000 elements, we need just 23 iterations. This is incredibly efficient.

# Implement a binary_search function that takes a list and a search item as arguments, and returns the index of the search item if found, or -1 otherwise. You may assume that the list argument will always be sorted.

# All of these examples should print True
# businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
#               'Donuts R Us', 'Eat a Lot', 'Good Food',
#               'Pasta Place', 'Pizzeria', 'Tiki Lounge',
#               'Zooper']
# print(binary_search(businesses, 'Pizzeria') == 7)
# print(binary_search(businesses, 'Apple Store') == 0)

# print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
# print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
# print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

# names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
#          'Tyler']
# print(binary_search(names, 'Peter') == -1)
# print(binary_search(names, 'Tyler') == 6)

"""
P
input = a list, and the element we are looking for
output = an integer (the index of the element we are looking for)
explicit = first, we have to find the middle element. If the middle element is the element we are looking for, stop. otherwise, get rid of the first half of the list (which includes the middle element). Find the middle element again. Repeat this process. The lists will be sorted!
implicit = 

E


D
lists

A
-high level algorithm: We will set a "high" variable and a "low" variable to keep track of the indexes we'll be checking at a time. We're also going to set a "mid" variable to keep track of the middle index of the list we are checking through. If the element is "less than" the value of the item we are looking for, then we will reset the "low" variable to check the latter half of the list. If the element is "more than" the item we are looking for, then we will reset the "high" variable to check the former half of the list. As we go through our iterations, the mid variable will continue to change, which will influence the condition of the while loop. As long as the low variable is less than or equal to the high variable the loop will continue its iterations. But if at any point this isnt true, this means that the while loop will break and it means that we couldn't find the item we were looking for; it will return -1.

-first, initialize a "high" variable, which is the same as the length of the list, minus 1, so this is equivalent to the index of the last element in the list
-initialize a "low" variable to 0, same as a starting index
-we are going to use a while loop to iterate through the list, since we want to keep searching through the list until our condition becomes false
    -within the loop, set a "mid" variable to represent the middle element index in the list. we'll calculate this by adding the low variable with the difference of high minus low, divided by 2
    -if the middle element is the same as the search item we are looking for
        -return that index
    -else if the element is "less than" the search item we are looking for
        -low will be reassigned to the mid index plus 1
        (the reason we can use "less than" is because all of the list arguments will be sorted beforehand; and don't forget we can search for string values less than others because it's comparing it lexicographically, so "Pete" would be "less than" "Peter")
    -else
        -the high variable will be reassigned to the mid variable minus 1
    
    -once the while loop stops running, if it doesn't return "mid", it will return -1

C
"""

def binary_search(lst, search_item):
    high = len(lst) - 1
    low = 0

    while low <= high:
        mid = low + (high - low) // 2
        if lst[mid] == search_item:
            return mid
        elif lst[mid] < search_item:
            low = mid + 1
        else:
            high = mid - 1

    return -1