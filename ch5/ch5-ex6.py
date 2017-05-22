def main():
    print("This program calculates the numeric value of a longer name.")
    name = input("Enter your name: ")
    merged_name = "".join(name.split())
    name_value = 0
    for letter in merged_name:
        name_value = name_value + ord(letter.lower()) - 96

    print("Your name is valued at {0}".format(name_value))

main()

