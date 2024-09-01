def clean_up(string):
    new_string = ""
    for chr in string:
        if chr.isalpha():
            new_string += chr
        elif new_string == "" or new_string[-1] != " ":
            new_string += " "

    return new_string

print(clean_up("---what's my +*& line?") == " what s my line ")