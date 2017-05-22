def main():
    print("This program encodes and decodes Caesar ciphers.")

    phrase = input("Enter a phrase to be encoded: ")
    key = eval(input("Enter a number to be the key: "))
    alphabet = "abcdefghijklmnopqrstuvwxyz" * 2 + "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 2
    encoded = ""
    decoded = ""
    words = []

    for word in phrase.split():
        for character in word:
            position = alphabet.find(character) + key
            encoded = encoded + alphabet[position]
        words.append(encoded)
        encoded = ""
    
    print("The encoded message is {0}".format(''.join(words)))

main()