
def longest_consecutive_ones(n):
    
    binary_representation = bin(n)[2:]
    

    consecutive_ones = binary_representation.split('0')
    longest = max(len(segment) for segment in consecutive_ones)
    
    return longest


try:
    number = int(input("Enter your number: "))
    longest_length = longest_consecutive_ones(number)
    print(f"Longest consecutive 1's length: {longest_length}")
except ValueError:
    print("Please enter a valid integer.")
