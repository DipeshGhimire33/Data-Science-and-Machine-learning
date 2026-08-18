import datetime

birth_date = datetime.date(2001, 5, 28)

print(birth_date)

today = datetime.datetime.now(tz=datetime.timezone.utc).date()

age = today.year - birth_date.year

if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

print(age)

print(datetime.datetime.fromtimestamp(1786935886, tz=datetime.timezone.utc).date())

print(datetime.date.fromisoformat("1998-12-04"))