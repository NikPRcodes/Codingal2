print("are you older than the age of 10? ")
print("1. yes")
print("2. No")
age1 = int(input("are you older than the age of 10? "))
if age1 == "1":
    print("Welcome")
else:
    age2 = int(input("Are you below the age of 20"))
    if age2 < 20:
        print("Welcome")
    else:
        print("You are too old try again in your next life ")