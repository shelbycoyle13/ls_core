# 48. Reverse and combine text
# Your task is to Reverse and Combine Words.
# Input: String containing different "words" separated by spaces
# 1. More than one word? Reverse each word and combine first with second, third with fourth and so on...(odd number of words => last one stays alone, but has to be reversed too)
# 2. Start it again until there's only one word without spaces
# 3. Return your result…

#print(reverse_and_combine_text("abc def") == "cbafed") 
#print(reverse_and_combine_text("dfghrtcbafed") == "dfghrtcbafed") 
#print(reverse_and_combine_text("234hh54 53455 sdfqwzrt rtteetrt hjhjh lllll12 44") ==
# "trzwqfdstrteettr45hh4325543544hjhjh21lllll")
#print(reverse_and_combine_text("sdfsdf wee sdffg 342234 ftt") == "gffds432243fdsfdseewttf")

"""
P
input = a string
output = a string
explicit = we want to reverse letters first. Then, conbine with a pair. Continue this process until there is only one word left. When one word is left, no more reversing needs to be done.
implicit = 

E

D
strings
list

A
    split the string by the whitespace

    while len(lst) > 1:
        
        reverse the words in the list, list comprehension
        
        combo_list = []
        for i in range(len(lst) - 1, 2) #we want to have a step of 2 to skip over every other word
            new_word = lst[i] + lst[i + 1]
            combo_list.append(new_word)

        if len(lst) % 2 == 1:
            combo_list.append(lst[-1])

    return combined_words[0]

C
"""

def reverse_and_combine_text(string):
    lst_of_words = string.split()

    while len(lst_of_words) > 1:

        reversed_words = [word[::-1] for word in lst_of_words]

        combo_list = []

        for i in range(0, len(reversed_words) - 1, 2):
            new_word = reversed_words[i] + reversed_words[i + 1]
            combo_list.append(new_word)

        if len(reversed_words) % 2 == 1:
                combo_list.append(reversed_words[-1])

    return combo_list[0]

print(reverse_and_combine_text("abc def") == "cbafed") 
# print(reverse_and_combine_text("dfghrtcbafed") == "dfghrtcbafed") 
# print(reverse_and_combine_text("234hh54 53455 sdfqwzrt rtteetrt hjhjh lllll12 44") ==
# "trzwqfdstrteettr45hh4325543544hjhjh21lllll")
# print(reverse_and_combine_text("sdfsdf wee sdffg 342234 ftt") == "gffds432243fdsfdseewttf")