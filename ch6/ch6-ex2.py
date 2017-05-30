def march(number):
    print("The ants go marching {0} by {0}, hurrah! hurrah!".format(number))

def marchshort(number):
    print("The ants go marching {0} by {0}".format(number))

def activity(user):
    print("{0}".format(user))

def ending():
    print("In the ground ...")
    print("To get out ...")
    print("Of the rain.")
    print("Boom! Boom! Boom!")

def inputs():
    number = input("Enter a number (written preferred): ")
    songactivity = input("Enter a activity: ")
    return number, songactivity

def main():
    number, user = inputs()
    march(number)
    march(number)
    marchshort(number)
    activity(user)
    ending()

main()


