class BeerSong:
    @classmethod
    def verse(cls, number):
        if number == 0:
            return "No more bottles of beer on the wall, no more bottles of beer.\n" "Go to the store and buy some more, 99 bottles of beer on the wall.\n"
        if number == 1:
            return "1 bottle of beer on the wall, 1 bottle of beer.\n" "Take it down and pass it around, no more bottles of beer on the wall.\n"
        if number == 2:
            return "2 bottles of beer on the wall, 2 bottles of beer.\n" "Take one down and pass it around, 1 bottle of beer on the wall.\n"
        else:
            return f"{number} bottles of beer on the wall, {number} bottles of beer.\n" f"Take one down and pass it around, {number - 1} bottles of beer on the wall.\n"
    
    @classmethod
    def verses(cls, start, end):
        final_string = []
        if start < 100 and 0 <= end < start:
            for num in range(start, end -1, -1):
                final_string.append(cls.verse(num))

        return "\n".join(final_string)

    @classmethod
    def lyrics(cls):
        return cls.verses(99, 0)