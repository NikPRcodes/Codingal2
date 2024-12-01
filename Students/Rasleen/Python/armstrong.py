num = int(input("Enter a number: "))
temp = num
sum_of_powers = 0
order = len(str(num))

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** order
    temp //= 10

if num == sum_of_powers:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")