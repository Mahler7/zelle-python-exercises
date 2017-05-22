def main():
    print("This program calculates the average length of words in a sentence.")
    sentence = input("Enter your sentence: ")
    letter_count = 0
    count_array = []
    for word in sentence.split():
        for characters in word:
            letter_count = letter_count + 1
        count_array.append(letter_count)
        letter_count = 0

    total_letters = 0
    for number in count_array:
        total_letters = total_letters + number

    average = total_letters / len(count_array)

    print("The average length of words in your sentence was {0}".format(average))

main()