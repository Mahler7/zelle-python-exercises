def main():
    print("This program turns phrases into acronyms.")
    phrase = input("Enter your phrase: ")
    letters = []
    for letter in phrase.split(" "):
        letters.append(letter[0].upper())

    acronym = "".join(letters)
    print("The acronym for the phrase {0} is {1}".format(phrase, acronym))

main()