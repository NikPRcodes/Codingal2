def is_power_of_two(n):
    
    return n > 0 and (n & (n - 1)) == 0

number = int(input("Enter a number: "))


if is_power_of_two(number):
    print(f"{number} is a power of 2.")
else:
    print(f"{number} is not a power of 2.")