import calendar

name=input("Enter your name")
print("Hello", name)
year=int(input("Please enter year to see calender"))
print(calendar.calendar(year))