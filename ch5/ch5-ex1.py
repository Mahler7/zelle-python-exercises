def main():
    day, month, year = eval(input("Enter day, month, and year numbers: "))

    date1 = str(month) + "/" + str(day) + "/" + str(year)

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    monthStr = months[month-1]

    date2 = monthStr + " " + str(day) + "," + str(year)

    print("The date is {0} or {1}.".format(date1, date2))

main()