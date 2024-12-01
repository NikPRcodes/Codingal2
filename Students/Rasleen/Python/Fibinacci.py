def fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence[:n]

num_terms = int(input("Enter the number of digits for which you want the fibonacci pattern: "))
if num_terms <= 0:
    print("Please, print a positive number")
else:
    print("Fibonacci sequence:", fibonacci(num_terms))

    