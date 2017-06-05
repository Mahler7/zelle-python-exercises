def bmi_evaluator(bmi):
    if bmi < 19:
        return "You're below the healthy range"
    elif bmi >= 19 and bmi <= 25:
        return "You're in a healthy range"
    elif bmi > 25:
        return "You're above the healthy range"

def bmi_calculator(height, weight):
    bmi = (weight * 720) / (height ** 2)
    return bmi

def inputs():
    height = eval(input("Enter your height in inches: "))
    weight = eval(input("Enter you weight in pounds: "))
    return height, weight

def intro():
    print("This program calculates a person's BMI")

def main():
    intro()
    height, weight = inputs()
    bmi = bmi_calculator(height, weight)
    healthy = bmi_evaluator(bmi)
    print("Your BMI score is {0:0.5f} and {1}".format(bmi,healthy))

main()