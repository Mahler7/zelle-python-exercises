def paid(hours, wages):
    money = 0
    overtime = 0
    if hours > 40:
        overtime = hours - 40
        money = (wages * 40) + (wages * 1.5 * overtime)
        return money
    elif hours < 40:
        money = (wages * hours)
        return money

def inputs():
    hours = eval(input("Enter the number of hours worked this week: "))
    wages = eval(input("Enter the hourly rate: "))
    return hours, wages

def intro():
    print("This program calculates the total wages for a week of work")

def main():
    intro()
    hours, wages = inputs()
    money = paid(hours,wages)
    print("For {0} hours worked this week, you earned {1:0.2f}".format(hours, money))

main()
