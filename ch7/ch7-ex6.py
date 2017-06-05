def above_ninety(speed_difference):
    fine = (speed_difference * 5) + 250
    return fine

def below_ninety(speed_difference):
    fine = (speed_difference * 5) + 50
    return fine

def speed_difference(speed_limit, drivers_speed):
    speed_difference = drivers_speed - speed_limit
    return speed_difference

def fine_calculator(speed_limit, drivers_speed):
    speeding_amount = speed_difference(speed_limit, drivers_speed)
    if drivers_speed > speed_limit and drivers_speed > 90:
        fine = above_ninety(speeding_amount)
        return fine
    elif drivers_speed > speed_limit and drivers_speed < 90:
        fine = below_ninety(speeding_amount)
        return fine
    elif drivers_speed <= speed_limit:
        return "Driver's speed was legal"

def fine_statement(speed_limit, drivers_speed, fine):
    if type(fine) != str:
        print("The driver was going {0} in a speed_limit of {1}, the fine is {2:0.2f}".format(drivers_speed, speed_limit, fine))
    else:
        print("Driver's speed was legal")

def inputs():
    speed_limit = eval(input("Please enter the speed limit: "))
    drivers_speed = eval(input("Please enter the driver's speed: "))
    return speed_limit, drivers_speed

def intro():
    print("This program calculates the penalty for speeding.")

def main():
    intro()
    speed_limit, drivers_speed = inputs()
    fine = fine_calculator(speed_limit, drivers_speed)
    fine_statement(speed_limit, drivers_speed, fine)
    

main()