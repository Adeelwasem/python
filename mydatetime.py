from datetime import date,time,datetime


todaydate = date.today()
currenttime = datetime.now()

print("Today's date is:", todaydate)
print("\n Current Date and Time is:", currenttime)


print("Date components:", todaydate.year,todaydate.month,todaydate.day)
print("Time:", currenttime)
