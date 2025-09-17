# Typoglycemia Generator

# Write a function that generates text following a pattern where:
# 1) the first and last characters of each word remain in their original place
# 2) characters between the first and last characters are sorted alphabetically
# 3) punctuation should remain at the same place as it started

# Examples:
# scramble_words('professionals') # should return 'paefilnoorsss'
# scramble_words("you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth.") # should return "you've gotta dacne like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth."

"""
P
input = a string
output = a string (but with the letters in a different order)
explicit = first and last letters stay in the same position. punctuation stays in the same position. The rest of the letters go in alphabetical order
implicit = 

E
scramble_words("rainbow" == "rabinow")

D
strings
loops

A
-create a helper function that's sole purpose is to scramble the words
    -if the length of the word is less than or equal to 3
        - return the word, since we're keeping the first and last char in place, and the middle char is already sorted
    -we'll assign variables for the first and last chars
    -the middle characters will be sorted by taking a slice of the word[1:-1]

-we'll make a list comprehension for just the letters inside of the middle section
-we'll create a sorted list of those same letters mentioned above

-create an empty list to represent the final middle
-create a letter index variable initialized at 0

-for every character in the middle section
    -if the char is alphabetic
        -we'll add the char to the mmiddle list
        - add 1 to the letter index
    -else if it's not alphabetic (i.e. punctuation or a space)
        -add the char to to the middle list
    
        -return the first + joined middle list + last

initialize an empty sentence list
initialize a current word that is an empty string

for every char in the text
    if char is alphanumeric or an apostrophe
        add the char to the current word
    else if it's not (i.e. maybe a period or a space)
        and if the current word is truthy
            append the current word to the final sentence list, but scramble it with the helper function
            reset the current word to an empty string
        otherwise if the current word is falsy, append the char to the final sentence list

finally, join the strings from the final sentence list together, and return


C
"""

def scramble_words(text):
    def scramble(word):
        if len(word) <= 3:  # Words of length <= 3 remain unchanged
            return word
        first, last = word[0], word[-1]
        middle = word[1:-1]

        # Separate letters and punctuation
        letters = [char for char in middle if char.isalpha()]
        sorted_letters = sorted(letters)  # Sort the letters only

        # Reconstruct the middle part with punctuation in place
        result_middle = []
        letter_index = 0
        for char in middle:
            if char.isalpha():
                result_middle.append(sorted_letters[letter_index])
                letter_index += 1
            else:
                result_middle.append(char)  # Preserve punctuation

        return first + ''.join(result_middle) + last

    # Process each word in the input
    result = []
    current_word = ""

    for char in text:
        if char.isalnum() or char == "'":  # Part of a word
            current_word += char
        else:  # Punctuation or space
            if current_word:  # Process the current word before punctuation
                result.append(scramble(current_word))
                current_word = ""
            result.append(char)  # Append the non-word character directly

    if current_word:  # Add the last word if there is one
        result.append(scramble(current_word))

    return ''.join(result)

# Examples
print(scramble_words('professionals') == 'paefilnoorsss')  
# Output: 'paefilnoorsss'

print(scramble_words("you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth.") == "you've gotta dacne like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth.")
# Output: "you've gotta dacne like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth."

