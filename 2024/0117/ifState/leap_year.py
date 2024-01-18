year = int(input())

isLeapYear: bool = False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            isLeapYear = True
        else:
            isLeapYear = False
    else:
        isLeapYear = True

if isLeapYear:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')