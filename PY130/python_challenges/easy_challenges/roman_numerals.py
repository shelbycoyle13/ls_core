class RomanNumeral:
    def __init__(self, year):
        self.year = year

    STRINGS_TO_NUMBERS = {
        1000 : "M",
        900: "CM",
        500 : "D",
        400: "CD",
        100 : "C",
        90: "XC",
        50 : "L",
        40: "XL",
        10 : "X",
        9: "IX",
        5 : "V",
        4: "IV",
        1 : "I"
    }

    def to_roman(self):
        new_string = ""
        still_need_to_convert = self.year

        for key, value in self.__class__.STRINGS_TO_NUMBERS.items():
            tuple1 = divmod(still_need_to_convert, key) #divmod returns (quotient, remainder) so i reused those names to make it easier to understand
            quotient = tuple1[0]
            remainder = tuple1[1]

            if quotient:
                new_string += value * quotient
            still_need_to_convert = remainder

        return new_string

