year = int(input("Enter the year : "))

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print(f"The year {year} is leap year.")
        else:
            print(f"The year {year} is a not leap year.")
    else:
        print(f"The year {year} is leap year.")
else:
    print(f"The year {year} is not a leap year.")