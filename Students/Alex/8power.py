a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))

result=(a&b)|((b|c)&(b&c))
print("The result is: ", result)