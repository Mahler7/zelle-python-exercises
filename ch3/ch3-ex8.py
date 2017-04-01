def main():
    print("This program calculates the Gregorian epact.")
    year = eval(input("Enter a four digit year: "))
    c = year // 100
    epact = (8 + (c // 4) - c + ((8 * c + 13) // 25) + 11 * (year % 19)) % 30
    print("The epact is", epact)

main()