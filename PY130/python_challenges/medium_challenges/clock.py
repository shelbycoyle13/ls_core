class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    @classmethod
    def at(cls, hour, minute=0):
        return cls(hour, minute)

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __add__(self, other): #Adds time together in minutes. If past midnight, we subtract time. Returns time back to hours:minutes
        minutes_since_midnight = self.compute_minutes_since_midnight() + other
        while minutes_since_midnight >= 1440:
            minutes_since_midnight -= 1440
        return self.compute_time_from(minutes_since_midnight)

    def __sub__(self, other):
        minutes_since_midnight = self.compute_minutes_since_midnight() - other
        while minutes_since_midnight < 0:
            minutes_since_midnight += 1440
        return self.compute_time_from(minutes_since_midnight)

    def __eq__(self, other):
        if not isinstance(other, Clock):
            raise TypeError
        return self.hour == other.hour and self.minute == other.minute

    def compute_minutes_since_midnight(self): #This converts your time into total minutes
        return (60 * self.hour) + self.minute

    def compute_time_from(self, minutes_since_midnight): #Converts minutes back to hours and minutes
        hours, minutes = divmod(minutes_since_midnight, 60)
        return Clock(hours, minutes)