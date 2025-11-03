class Octal:
    def __init__(self, string):
        self.string = string

    def to_decimal(self):
        if not self.string.isnumeric():
            return 0
        if any(char in "89" for char in self.string):
            return 0
        reversed_list = reversed(self.string)

        final_sum = 0
        
        for exp, char in enumerate(reversed_list):
            final_sum += int(char) * (8**exp)

        return final_sum