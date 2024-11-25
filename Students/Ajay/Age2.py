try:
    age = int(input("what is your age? : "))
    if age % 2 == 0:
        print("your age is an even number")
    else:
        print("your age is an odd number")
except ValueError as a:
    print("exception: ",a)
