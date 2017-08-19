def removeDuplicates(myList):
    uniqueList = []
    for i in myList:
        if i not in uniqueList:
            uniqueList.append(i)
    return uniqueList

def main():
    myList = [1,2,2,3,3,3,4,5,5,6,7,8,8,8,8,9,10]
    uniqueList = removeDuplicates(myList)
    print(uniqueList)

main()