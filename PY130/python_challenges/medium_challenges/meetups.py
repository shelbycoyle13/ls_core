from datetime import date, timedelta

class Meetup:
    DAY_OF_WEEK = {
    'monday': 0,
    'tuesday': 1,
    'wednesday': 2,
    'thursday': 3,
    'friday': 4,
    'saturday': 5,
    'sunday': 6,
}
    
    SCHEDULE_START_DAY = {
    'first': 1,
    'second': 8,
    'third': 15,
    'fourth': 22,
    'fifth': 29,
    'teenth': 13,
    'last': None,
}
    
    def __init__(self, year, month):
        self.year = year
        self.month = month
        if self.month == 12:
            last_day_of_the_month = date(self.year + 1, 1, 1) - timedelta(days=1)
        else:
            last_day_of_the_month = date(self.year, self.month + 1, 1) - timedelta(days=1)
        self.days_in_month = last_day_of_the_month.day #The last day of the month gives us the total days in the month anyway


    def day(self, day_name, place):
        day_name = day_name.lower()
        place = place.lower()

        if place == "last":
            start_day = self.days_in_month - 6
            last_day = self.days_in_month
        else:
            start_day = self.SCHEDULE_START_DAY[place]
            last_day = min(start_day + 6, self.days_in_month)

        for date_digit in range(start_day, last_day + 1):
            date_obj = date(self.year, self.month, date_digit)
            if date_obj.weekday() == self.DAY_OF_WEEK[day_name]:
                return date_obj

        