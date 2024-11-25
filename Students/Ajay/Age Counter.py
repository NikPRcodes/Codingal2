try:
    age = eval(input("what is your age? : "))
except ValueError as a:
    print("exception: ",a)
if age % 2 == 0:
    print("your age is an even number")
else:
    print("your age is an odd number")