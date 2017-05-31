def squareEach(nums):
    squaredNums = []
    for num in nums:
        squaredNums.append(num ** 2)
    return squaredNums

def intro():
    print("This program modifies a list by squaring each entry")

def main():
    intro()
    nums = [1,2,3,4,5,6,7,8]
    squaredNums = squareEach(nums)
    print("Your squared sums list", squaredNums)

main()