def binary_to_decimal():
    while True:
        binary_input = input("Enter your Binary (or 'exit' to quit): ")
        if binary_input.lower() == 'exit':
            break
        try:
            decimal_output = int(binary_input, 2)
            print(f"Binary: {binary_input} Decimal: {decimal_output}")
        except ValueError:
            print("Invalid binary number. Please enter only 0's and 1's.")

binary_to_decimal()