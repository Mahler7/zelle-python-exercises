def eligibility(age, citizenship):
    if age >= 30 and citizenship >= 9:
        return "is eligibile to be a Senator or Congressman"
    elif age >= 25 and citizenship >= 7:
        return "is eligibile to be a Congressman"
    else:
        return "is not eligibile to be a Congressman or Senator"

def inputs():
    age = eval(input("Enter the person's age: "))
    citizenship = eval(input("Enter the number of years the person has been a U.S. citizen: "))
    return age, citizenship

def intro():
    print("This program determines if a person is elligible for running in the House or Senate")

def main():
    intro()
    age, citizenship = inputs()
    government_eligibility = eligibility(age, citizenship)
    print("The person {0}".format(government_eligibility))

main()
