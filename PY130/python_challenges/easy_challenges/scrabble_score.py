class Scrabble:
    POINTS = {
        "AEIOULNRST" : 1,
        "DG" : 2,
        "BCMP" : 3,
        "FHVWY" : 4,
        "K" : 5,
        "JX" : 8,
        "QZ" : 10
    }

    def __init__(self, move):
        self.move = move

    def score(self):
        final_score = 0
        if not self.move:
            return 0
        if not self.move.isalpha():
            return 0
        for letter in self.move.upper():
            for key, value in self.POINTS.items():
                if letter in key:
                    final_score += value

        return final_score
        
    @classmethod
    def calculate_score(cls, move):
        return cls(move).score()