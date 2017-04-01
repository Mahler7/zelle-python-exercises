def main():
    print("This program determines the average of a sum of numbers entered by a user.")
    n = eval(input("How many numbers would you like to average: "))
    sum = 0
    for i in range(n):
        number = eval(input("Enter a number: "))
        sum = sum + number
    average = sum / n
    print("Your average is", float(average))

main()