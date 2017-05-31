def acronym(phrase):
    letters = []
    for letter in phrase.split(" "):
        letters.append(letter[0].upper())

    acronym = "".join(letters)
    return acronym

def inputs():
    phrase = input("Enter your phrase: ")
    return phrase

def intro():
    print("This program turns phrases into acronyms.")

def main():
    intro()
    phrase = inputs()
    phraseAcronym = acronym(phrase)
    print("The acronym for the phrase {0} is {1}".format(phrase, phraseAcronym))

main()