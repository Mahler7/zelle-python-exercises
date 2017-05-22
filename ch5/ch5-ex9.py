def main():
    print("This program calculates the number of words in a sentence.")
    sentence = input("Enter your sentence: ")
    words = sentence.split()
    print("This sentence has {0} words".format(len(words)))

main()