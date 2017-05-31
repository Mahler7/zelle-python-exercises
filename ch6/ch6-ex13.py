def toNumbers(strList):
    number_list = []
    for word in strList:
        number_list.append(len(word))
    return number_list

def intro():
    print("This program converts a list of a strings to a number")

def main():
    string_list = ["hello", "how", "are", "you", "doing", "good"]
    intro()
    number_list = toNumbers(string_list)
    print("Your list of numbers is", number_list)

main()
