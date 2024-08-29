# Write a function that takes a short line of text and prints it within a box.

def print_in_box(s, max_width=float('inf')):
    length = len(s)

    if length > max_width:
        s = s[:max_width + 1]

    border_top = ''
    padding_top = ''
    padding_bottom = ''
    border_bottom = ''

    for chr in s:
        border_top += "-"
        padding_top += " "
        padding_bottom += " "
        border_bottom += "-"

    print(f"+-{border_top}-+")
    print(f"| {padding_top} |")
    print(f"| {s} |")
    print(f"| {padding_bottom} |")
    print(f"+-{border_bottom}-+")


# print_in_box("Modify this function so that it truncates the message if it doesn't fit inside a maximum width provided as a second argument (the width is the width of the box itself). You may assume no maximum if the second argument is omitted.", 10)
# print_in_box('To boldly go where no one has gone before.')

# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

# print_in_box('')

# +--+
# |  |
# |  |
# |  |
# +--+

# Further Exploration
# Modify this function so that it truncates the message if it doesn't fit inside a maximum width provided as a second argument (the width is the width of the box itself). You may assume no maximum if the second argument is omitted.

# For a challenging but fun exercise, try word wrapping messages that are too long to fit, so that they appear on multiple lines but are still contained within the box. This isn't an easy problem, but it's doable with basic Python.

def print_in_box(s, max_width=float('inf')):
    length = len(s)

    if length > max_width:
        word_wrapped_string = ''
        index = 0
        while index < len(s):
            piece = s[index:max_width + 1]
            word_wrapped_string += piece            
            index += max_width
            
        

    border_top = ''
    padding_top = ''
    padding_bottom = ''
    border_bottom = ''

    for chr in s:
        border_top += "-"
        padding_top += " "
        padding_bottom += " "
        border_bottom += "-"

    print(f"+-{border_top}-+")
    print(f"| {padding_top} |")
    print(f"| {s} |")
    print(f"| {padding_bottom} |")
    print(f"+-{border_bottom}-+")

print_in_box("Modify this function so that it truncates the message if it doesn't fit inside a maximum width provided as a second argument (the width is the width of the box itself). You may assume no maximum if the second argument is omitted.", 50)