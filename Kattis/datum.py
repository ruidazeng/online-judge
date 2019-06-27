from datetime import datetime, date, time

days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
]

d, m = [int(x) for x in input().split()]
myDate = date(2009, m, d)
print(days[myDate.weekday()])