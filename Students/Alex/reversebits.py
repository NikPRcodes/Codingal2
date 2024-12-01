def reverse_bits(n):
    
    binary_representation = bin(n)[2:]
    
    reversed_binary = binary_representation[::-1]
    
    reversed_number = int(reversed_binary, 2)
    return reversed_number


original_number = int(input("Enter your original number: "))
result = reverse_bits(original_number)


print(f"Reversed Number: {result}")