class Anagram:
    def __init__(self, word_arg):
        self.word_arg = word_arg.lower()
    
    def match(self, list1):
        new_list = []
        for word in list1:
            if self.word_arg != word.lower() and sorted(word.lower()) == sorted(self.word_arg):
                new_list.append(word)

        return new_list
