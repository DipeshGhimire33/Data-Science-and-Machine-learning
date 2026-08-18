import datetime

today = datetime.date.today
print(today)

dt =datetime.datetime(2025, 12 ,3 ,8 ,29 ,55,tzinfo=datetime.timezone.utc )
print(dt)


today = datetime.datetime.now(datetime.timezone.utc)
print(today)

print(today - dt)

#time delta

year_5 = datetime.timedelta(days= 5 * 365)

print(today - year_5)
