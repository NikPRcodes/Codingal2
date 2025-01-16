def loop(n):
    # First Loop
    for i in range(0, n+1):  # Loops from 0 to n (inclusive)
        print("First Loop")

    # Second Loop
    j = 1
    while j <= n+1:  # Doubles j each iteration until it exceeds n+1
        print("Second Loop", j)
        j = j * 2

    # Third Loop
    for i in range(0, 100):  # Runs exactly 100 times
        print("Third Loop")


loop(7)