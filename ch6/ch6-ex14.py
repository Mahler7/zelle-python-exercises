def squareEach(nums):
    squaredNums = []
    for num in nums:
        squaredNums.append(int(num) ** 2)
    return squaredNums

def sumList(nums):
    total = 0
    for num in nums:
        total = total + num
    return total

def getFile():
    infileName = input("Enter a file to open: ")
    infile = open(infileName, 'r')
    return infile

def intro():
    print("This program adds the squares of numbers from a file")

def main():
    intro()
    infile = getFile()
    squaredNums = squareEach(infile)
    sumTotal = sumList(squaredNums)
    print("This is the sum of the squares of the file:", sumTotal)

main()