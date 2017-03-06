def main():
    print("This program determines the distance to a lightning strike.")
    s = eval(input("Please enter the number of seconds between the flash and the sound of thunder: "))
    distance = (1100 * s) / 5280
    print("The lightning strike is", distance, "miles away.")

main()