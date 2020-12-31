import datetime
import calendar


def meetup(year, month, week, day_of_week):
    day = 1
    weekday_key = {"Monday": 0,
                   "Tuesday": 1,
                   "Wednesday": 2,
                   "Thursday": 3,
                   "Friday": 4,
                   "Saturday": 5,
                   "Sunday": 6}

    ordinal = {"1st": 0, "2nd": 1, "3rd": 2, "4th": 3, "5th": 4}

    weekdays_in_month = []

    if week == "teenth":
        for i in range(13, 20):
            if datetime.datetime(year, month, i).weekday() == weekday_key[day_of_week]:
                return (datetime.date(year, month, i))
    elif week == "last":
        day = (calendar.monthcalendar(year, month)[-1][weekday_key[day_of_week]])
        if day == 0:
            day = (calendar.monthcalendar(year, month)[-2][weekday_key[day_of_week]])

    else:
        for i in calendar.monthcalendar(year, month):
            weekdays_in_month.append(i[weekday_key[day_of_week]])
        if 0 in weekdays_in_month:
            weekdays_in_month.remove(0)
        day = weekdays_in_month[ordinal[week]]

    return (datetime.date(year, month, day))