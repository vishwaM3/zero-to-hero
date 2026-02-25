days=int(input("enter a total days:"))
year=days/365
temp=days%365
month=temp/30
redays=temp%30
print("Year:",year)
print('Month:',month)
print("readys:",redays)