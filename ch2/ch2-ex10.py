def main():
    print("This program converts pounds to kilograms.")
    pounds = eval(input("Enter the number of pounds: "))
    kilograms = pounds * (1 / 2.204)
    print(pounds, "pounds =", kilograms, "kilograms")
main()