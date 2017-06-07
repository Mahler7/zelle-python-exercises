def easter_april(d, e):
    easter_date = d + e - 9
    return "Easter is on April {0}".format(easter_date)

def easter_march(d, e):
    easter_date = d + e
    return "Easter is on March {0}".format(easter_date)

def easter_print(d, e):
    if 22 + d + e > 31:
        date = easter_april(d, e)
        return date
    elif 22 + d + e < 31:
        date = easter_march(d, e)
        return date

def easter_calculator(year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    date = easter_print(d, e)
    return date

def inputs():
    validYear = False
    while validYear == False:
        year = eval(input("Enter a year between 1982 and 2048: "))
        if year >= 1982 and year <= 2048:
            validYear == True
            return year
        else:
            validYear == False
        
def intro():
    print("This program figures out the date of Easter between the years 1982 and 2048")

def main():
    intro()
    year = inputs()
    date = easter_calculator(year)
    print(date)

main()
