# Count of Pairs

# Write a function that takes a list of integers as input and counts the number of
# pairs in the list. A pair is defined as two equal integers separated by some
# other integer(s).

# Examples:
# pairs([1, 2, 5, 6, 5, 2]) --> 2
# pairs([1, 2, 2, 20, 6, 20, 2, 6, 2]) --> 4

"""
P
input = a list of integers
output = an integer
explicit = a pair is a pair of the same number, but separated by another integer(s) in between
implicit = it appears as though once you "use" an integer in a pair, you can't "use" it again to count another pair. I.e, you can't use two pairs of 2's.

E
# pairs([1, 2, 3, 4, 1, 2, 3]) --> 3

D
list

A
-Since we need to count how many pairs there are, let's initialize a count variable to 0
-we want to be able to not re-use an integer more than just 1 pair, so let's initialize a dictionary
-we definitely want to iterate through the index and the element of the list; let's use enumerate
    -if the number is in the dictionary already (as a key)
        -let's make sure that the next number will have a buffer number in between; if the current index we are at minus the index of the previous index of the same key is greater than 1
            -add +1 to the count
            -then we also want to reset the tracking for that key to the current index. Essentially, we are "sliding" through this list; each time we find a pair, we update the most recent index for that integer / key
    -else if the number if not in the dictionary
        -add it as a key
    -return the final count


C
"""

def pairs(lst):
    pair_count = 0
    last_seen = {}  # Dictionary to track the last index of each number

    for i, num in enumerate(lst):
        if num in last_seen:
            # Check if the current index is separated from the last index
            if i - last_seen[num] > 1:
                pair_count += 1
                # Reset the tracking for this number since this pair is counted
                last_seen[num] = i
        else:
            # Track the first occurrence of the number
            last_seen[num] = i

    return pair_count

# Test cases
print(pairs([1, 2, 5, 6, 5, 2]))  # Output: 2
print(pairs([1, 2, 2, 20, 6, 20, 2, 6, 2]))  # Output: 4
print(pairs([1, 2, 3, 4, 1, 2, 3]))
