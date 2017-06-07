def easter_april(d, e, year):
    yearCheck = year_exception_checker(year)
    if yearCheck == True:
        easter_date = d + e - 16
        if easter_date <= 0:
            easter_date = 31 + easter_date
            return "Easter is on March {0}".format(easter_date)
        elif easter_date > 0:
            return "Easter is on April {0}".format(easter_date)
    elif yearCheck == False:
        easter_date = d + e - 9
        return "Easter is on April {0}".format(easter_date)

def easter_march(d, e, year):
    if yearCheck == True:
        easter_date = d + e - 7
        return "Easter is on March {0}".format(easter_date)
    elif yearCheck == False:
        easter_date = d + e
        return "Easter is on March {0}".format(easter_date)

def easter_print(d, e, year):
    if 22 + d + e > 31:
        date = easter_april(d, e, year)
        return date
    elif 22 + d + e < 31:
        date = easter_march(d, e, year)
        return date

def year_exception_checker(year):
    if year == 1954 or year == 1981 or year == 2049 or year == 2076:
        return True
    else:
        return False

def easter_calculator(year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    date = easter_print(d, e, year)
    return date

def inputs():
    validYear = False
    while validYear == False:
        year = eval(input("Enter a year between 1900 and 2099: "))
        if year >= 1900 and year <= 2099:
            validYear == True
            return year
        else:
            validYear == False
        
def intro():
    print("This program figures out the date of Easter between the years 1900 and 2099")

def main():
    intro()
    year = inputs()
    date = easter_calculator(year)
    print(date)

main()
