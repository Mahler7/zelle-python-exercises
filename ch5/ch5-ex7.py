def main():
    print("This program encodes and decodes Caesar ciphers.")

    word = input("Enter a word to be encoded: ")
    key = eval(input("Enter a number to be the key: "))
    encoded = ""
    decoded = ""
    for character in word:
        encoded = encoded + chr(ord(character) + key)

    print("The encoded message is {0}".format(encoded))

    for character in encoded:
        decoded = decoded + chr(ord(character) - key)

    print("The decoded message is {0}".format(decoded))

main()