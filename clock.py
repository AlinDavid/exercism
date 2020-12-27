class Clock:
    def __init__(self, hour, minute):
        self.hour = hour + minute // 60
        self.minute = minute % 60

    def __repr__(self):
        return "The time is {} and {} minutes".format(self.hour, self.minute)

    def __eq__(self, other):
        return self.minutes == other.minutes and self.hours == other.hours

    def __add__(self, minutes):
        self.hour += minutes // 60
        minutes = minutes % 60
        if minutes + self.minute > 60:
            self.hour += (minutes + self.minute) // 60
            self.minute = (self.minute + minutes) % 60
        else:
            self.minute += minutes

    def __sub__(self, minutes):
        self.hour -= minutes // 60
        minutes = minutes % 60
        if self.minute - minutes < 0:
            self.hour -= (minutes + self.minute) // 60
            self.minute = 60 + (self.minute - minutes)
        else:
            self.minute -= minutes