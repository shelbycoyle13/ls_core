# Write a function that takes a short line of text and prints it within a box.

# def print_in_box(s, max_width=float('inf')):
#     length = len(s)

#     if length > max_width:
#         s = s[:max_width + 1]

#     border_top = ''
#     padding_top = ''
#     padding_bottom = ''
#     border_bottom = ''

#     for chr in s:
#         border_top += "-"
#         padding_top += " "
#         padding_bottom += " "
#         border_bottom += "-"

#     print(f"+-{border_top}-+")
#     print(f"| {padding_top} |")
#     print(f"| {s} |")
#     print(f"| {padding_bottom} |")
#     print(f"+-{border_bottom}-+")


# print_in_box("A long, long time ago, I can still remember how that music Used to make me smile And I knew if I had my chance That I could make those people dance And maybe they'd be happy for a while", 10)

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
    string_length = len(s)
        
    word_wrapped_string = []
    index = 0

    while index < string_length:
        line = s[index: index + max_width]
        word_wrapped_string.append(line)
        index += max_width
        
    border_top = '-' * max_width
    padding_top = ' ' * max_width
    padding_bottom = padding_top
    border_bottom = border_top

    print(f"+-{border_top}-+")
    print(f"| {padding_top} |")
    for line in word_wrapped_string:
        print(f"| {line.ljust(max_width)} |")
    print(f"| {padding_bottom} |")
    print(f"+-{border_bottom}-+")

print_in_box("A long, long time ago, I can still remember how that music Used to make me smile And I knew if I had my chance That I could make those people dance And maybe they'd be happy for a while", 50)