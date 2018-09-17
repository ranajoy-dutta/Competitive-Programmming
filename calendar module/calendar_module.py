import calendar
month, date, year = map(int, input().split())
day = calendar.weekday(year, month, date)
if day == 0:
    print("MONDAY")
elif day == 1:
    print("TUESDAY")
elif day == 2:
    print("WEDNESDAY")
elif day == 3:
    print("THURSDAY")
elif day == 4:
    print("FRIDAY")
elif day == 5:
    print("SATURDAY")
else:
    print("SUNDAY")
