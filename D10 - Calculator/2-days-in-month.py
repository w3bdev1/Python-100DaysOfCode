def is_leapyear(year):
    """Check whether a year is leap year or not and return appropriate boolean"""
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    """Returns the days in a month for a given year"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month < 1 or month > 12:
        print("Month has be between 1 and 12")
        return

    if month == 2 and is_leapyear(year):
        return 29
    else:
        return month_days[month - 1]


year = int(input("Year: "))
month = int(input("Month: "))
print(f"There are {days_in_month(year, month)} days in this month.")