def sumList(nums):
    total = 0
    for num in nums:
        total = total + num
    return total

def intro():
    print("This program modifies a list by adding each entry")

def main():
    intro()
    nums = [1,2,3,4,5,6,7,8]
    sumNums = sumList(nums)
    print("Your sum of your list is", sumNums)

main()