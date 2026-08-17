import datetime

birth_date = datetime.date(2001, 5, 28)
print(birth_date)

today = datetime.date.today()

age = today - birth_date
age = age.days // 365
print(age)


print(datetime.date.fromtimestamp(1786935886))
print(datetime.date.fromisoformat("1998-12-04"))