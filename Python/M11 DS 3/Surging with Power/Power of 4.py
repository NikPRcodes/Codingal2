def powerOf4(number):
    count = 0
    if(number&(~(number&(number-1)))):
        while(number>1):
            number>>=1
            count+=1
        
        if(count%2 == 0):
            return True
        else:
            return False
        
number = int(input("Enter a number: "))
if(powerOf4(number)):
    print(f"{number} is a Power of 4")
else:
    print(f"{number} is not a Power of 4")