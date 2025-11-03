class DNA:
    def __init__(self, string):
        self.string = string

    def hamming_distance(self, string2):
        differences = 0

        for a, b in zip(self.string, string2):
            if a != b:
                differences += 1
        
        return differences