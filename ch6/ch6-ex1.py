def oldmacdonald():
    print("Old McDonald Had a Farm, Ee-igh, Ee-igh, Oh!")

def oldanimal(animal):
    print("And on that farm he had an {0}, Ee-igh, Ee-igh, Oh!".format(animal))

def oldanimalsound(sound):
    print("With a {0}, {0} here and a {0}, {0} there.".format(sound))
    print("Here a {0}, there a {0}, everywhere a {0}, {0}".format(sound))

def main():
    oldmacdonald()
    oldanimal("cow")
    oldanimalsound("moo")
    oldmacdonald()
    print()
    oldmacdonald()
    oldanimal("dog")
    oldanimalsound("bark")
    oldmacdonald()
    print()
    oldmacdonald()
    oldanimal("cat")
    oldanimalsound("meow")
    oldmacdonald()
    print()
    oldmacdonald()
    oldanimal("chicken")
    oldanimalsound("cluck")
    oldmacdonald()
    print()
    oldmacdonald()
    oldanimal("horse")
    oldanimalsound("neigh")
    oldmacdonald()
    print()

main()