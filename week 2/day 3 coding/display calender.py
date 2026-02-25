import calendar
year = int(input("Enter year: "))
month = int(input("Enter month: "))
month_list= calendar.month(year, month)
print(month_list)