def is_century_year(year):
    if year % 100 == 0:
        return True
    else:
        return False

def leap_year_calculator(year):
    century_year = is_century_year(year) 
    
    if century_year == True:
        if year % 400 == 0:
            return "{0} is a leap year.".format(year)
        else:
            return "{0} is not a leap year.".format(year)
    elif century_year == False:
        if year % 4 == 0:
            return "{0} is a leap year.".format(year)
        else:
            return "{0} is not a leap year.".format(year)

def inputs():
    try:
        year = eval(input("Enter a year: "))
        return year
    except NameError:
        print("A year must be a number")

def intro():
    print("This program determines whether a year is a leap year")

def main():
    intro()
    year = inputs()
    leap_year = leap_year_calculator(year)
    print(leap_year)

main()