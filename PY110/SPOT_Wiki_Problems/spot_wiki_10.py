# Write a function that, given a string of text, returns a list of the top-3 most
# occurring words, in descending order of the number of occurrences.

# Assumptions:
# - A word is a string of letters (A to Z) optionally containing one or more apostrophes (').
# - Matches should be case-insensitive.
# - Ties may be broken arbitrarily.
# - If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty list if a text contains no words.

# Examples:
# top_3_words(" , e .. ") # ["e"]
# top_3_words(" ... ") # []
# top_3_words(" ' ") # []
# top_3_words(" ''' ") # []
# top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
# mind, there lived not long since one of those gentlemen that keep a lance
# in the lance-rack, an old buckler, a lean hack, and a greyhound for
# coursing. An olla of rather more beef than mutton, a salad on most
# nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
# on Sundays, made away with three-quarters of his income.""") # should return ["a", "of", "on"]

"""
P
input = a string
output = a list (of the top 3 most occuring words)
explicit = a word is classified as a word if it has a string of letters from a-z and can contain 1 or more '. if there's less than 3 unique words, we'll return the top 2 or top 1 word(s). we're returning the words in descending order based on the number of occurrences
implicit = 

E

D
strings
lists

A
-[string.count(word) for word in string]
-we then want to sort this list in descending order; can use reversed = True

C
"""
def top_3_words(string):
    # Step 1: Normalize the input
    normalized = string.lower()
    for char in ",.!?;:": #Just typical punctuation marks
        normalized = normalized.replace(char, " ") #replace the character with a space
    
    # Step 2: Split into words
    words = normalized.split()
    
    # Step 3: Filter out invalid words
    valid_words = []
    for word in words:
        if word.strip("'"):  # Remove words that are only apostrophes or empty
            valid_words.append(word)
    
    # Step 4: Count word occurrences
    word_counts = {}
    for word in valid_words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    # Step 5: Sort by count and get the top 3 words
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True) #Because .items returns a tuple, key lambda means it is getting the first index from the tuple, which means it is sorting by the count (i.e. the integer)
    return [word for word, count in sorted_words[:3]] #Here we only want the top 3 words, hence the slicing

# Examples
print(top_3_words(" , e .. "))  # ["e"]
print(top_3_words(" ... "))  # []
print(top_3_words(" ' "))  # []
print(top_3_words(" ''' "))  # []
print(top_3_words("""
In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.
"""))
# Output: ["a", "of", "on"]