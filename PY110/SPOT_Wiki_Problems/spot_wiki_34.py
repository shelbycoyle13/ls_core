# 34. Do the Wave
# Create a function that turns a string into a Wave. You will be passed a string and you must return that string in a list where an uppercase letter is a person standing up.

#print(wave("hello") == ["Hello", "hEllo", "heLlo", "helLo", "hellO"])
#print(wave("") == [])
#print(wave("two words") == ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"])
#print(wave(" gap ") == [" Gap ", " gAp ", " gaP "])

"""
P
input = a string
output = a list (of strings)
explicit = we want to take a string and return a list with copies of the string. each copy will have a capital letter in each letter, one at a time, consecutively. so the length of the list of strings is the same as the length of the original string, minus whitespace
implicit = empty string = empty list. if a string has multiple words, we can skip over the space in between them and move onto the next letter to capitalize it

E

D
strings
lists

A
final_list = []

for i, letter in enumerate(string)
    word_copy = ""
        if letter.isalpha
            for j in range(len(string))
                uppercase_letter = string[j].upper()
                word_copy += uppercase_letter
            word_copy += letter
        else
            continue
    final_list.append(word_copy)
    
    return final_list

C
"""

def wave(string):
    final_list = []

    for i, letter in enumerate(string):
        if letter.isalpha():
            word_copy = string[:i] + letter.upper() + string[i + 1:] #Construct the new word one piece at a time. Start with the beginning piece of the word. Then capitalize the current letter at the current index. Finally, add the slice of the rest of the word, starting one away from the current index and slice to the end of the word
            final_list.append(word_copy)
    
    return final_list
    

print(wave("hello")) # == ["Hello", "hEllo", "heLlo", "helLo", "hellO"])
#print(wave("") == [])
#print(wave("two words") == ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"])
#print(wave(" gap ") == [" Gap ", " gAp ", " gaP "])