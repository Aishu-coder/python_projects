#my format_name(f_name,l_name)
#f=f_name.title()
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(given_year, given_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_or_nonleap = is_leap(given_year)
    if leap_or_nonleap == True and given_month == 2:# if is_leap(year):
        return 29
    elif leap_or_nonleap == False:
        return month_days[given_month - 1]

year = int(input())  # Enter a year
month = int(input())  # Enter a month
days = days_in_month(year, month)
print(days)

