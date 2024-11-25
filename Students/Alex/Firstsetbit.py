def rightmost_set_bit_position(n):
    if n == 0:
        return "No set bits"
    
    
    rightmost_bit = n & -n
    
    
    position = 1
    while rightmost_bit > 1:
        rightmost_bit >>= 1
        position += 1
    
    return position


try:
    number = int(input("Enter number: "))
    position = rightmost_set_bit_position(number)
    print(f"Position of the first set bit: {position}")
except ValueError:
    print("Please enter a valid integer.")