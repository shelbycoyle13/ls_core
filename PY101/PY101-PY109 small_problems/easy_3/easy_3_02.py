# Write a function that takes a string argument and returns a new string that contains the value of the original string with all consecutive duplicate characters collapsed into a single character.

def crunch(string):
    new_string = ''
    index = 0

    while index < len(string):
        if index == len(string) - 1 or string[index] != string[index + 1]:
            new_string += string[index]
            
        index += 1
    return new_string

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')