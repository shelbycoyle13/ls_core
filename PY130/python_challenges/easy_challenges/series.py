class Series:
    def __init__(self, string):
        self.string = string

    def slices(self, slice_length):
        if slice_length > len(self.string):
            raise ValueError
        list_of_matching_strings = [self.string[num1:num2] for num1 in range(len(self.string))
                                        for num2 in range(1, len(self.string) + 1)
                                        if len(self.string[num1:num2]) == slice_length]

        final_list = []
        for string in list_of_matching_strings:
            sublist = []
            for char in string:
                sublist.append(int(char))
            final_list.append(sublist)
        return final_list   