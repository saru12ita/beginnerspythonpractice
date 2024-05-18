#python program to check the leap year
year=int(input("Enter any year="))

if ((year%100==0) and (year%400==0)):
    print(f"The {year} is leap year",year)

elif((year%4==0) and ((year%100)!=0)):
    print(f"The {year} is leap year",year)

else:
    print(f"The {year} is not leap year",year)