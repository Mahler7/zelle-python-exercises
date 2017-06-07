def print_date_number(dayNum):
    return "It is day {0}".format(dayNum)

def date_number(month, date, year):
    dayNum = 31 * (month - 1) + date
    century_year = is_century_year(year)
    if month > 2 and century_year == False:
        dayNum = dayNum - (4 * (month) + 23) // 10
        return dayNum
    elif month > 2 and century_year == True:
        dayNum = dayNum - ((4 * (month) + 23) // 10) + 1
        return dayNum
    else:
        return dayNum

def print_date(validDate, month, date, year):
    if validDate:
        return "{0}/{1}/{2} is a valid date".format(month, date, year)
    else:
        return "{0}/{1}/{2} is not a valid date".format(month, date, year)

def is_century_year(year):
    if year % 100 == 0:
        return True
    else:
        return False

def valid_date(month, date, year):
    print("Hello")
    century_year = is_century_year(year)
    if month == 2 and century_year == False:
        if date <= 28:
            return True
        else:
            return False
    elif month == 2 and century_year == True:
        if date <= 29:
            return True
        else:
            return False
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if date <= 30:
            return True
        else:
            return False
    else:
        return True

def get_year():
    try:
        year = eval(input("Enter a year: "))
    except NameError:
        print("Please enter a valid number")
    return year

def get_day():
    validDay = False
    while validDay == False:
        try:
            day = eval(input("Enter a day: "))
            if day > 0 and day < 31:
                validDay = True
            else: 
                validDay = False
        except NameError:
            print("Please enter a valid number")
    return day

def get_month():
    validMonth = False
    while validMonth == False:
        try:
            month = eval(input("Enter a month: "))
            if month > 0 and month < 13:
                validMonth = True
            else:
                validMonth = False
        except NameError:
            print("Please enter a valid number")   
    return month

def inputs():
    month = get_month()
    day = get_day()
    year = get_year()   
    return month, day, year

def intro():
    print("This program determines whether or not a date is valid and calculates the corresponding day number")

def main():
    intro()
    month, day, year = inputs()
    validDate = valid_date(month, day, year)
    dayNum = date_number(month, day, year)
    date_validity = print_date(validDate, month, day, year)
    date_num = print_date_number(dayNum)
    print(date_validity)
    print(date_num)

main()