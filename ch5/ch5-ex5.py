def main():
    print("This program calculates the numeric value of a single name.")
    name = input("Enter your name: ")
    name_value = 0
    for letter in name:
        name_value = name_value + ord(letter.lower()) - 96

    print("Your name is valued at {0}".format(name_value))

main()