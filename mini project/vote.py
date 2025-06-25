# write a python program to check if a person is eligible to vote or not.

# age=int(input('enter your age: '))


def check_eligibility(age):
    if age>=18:
        print("elligible to vote")

    else:
        print("not elligible to vote")
    

check_eligibility(10)
check_eligibility(18)
check_eligibility(30)


