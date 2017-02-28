def main():
    print("This program converts Celsius temperatures into Fahrenheit.")

    celsius = 0
    for i in range(10):
        
        fahrenheit = 9/5 * celsius + 32
        celsius = celsius + 10
        print("The temperature is", celsius, "degrees Celsius and", fahrenheit, "degrees Fahrenheit.")

main()