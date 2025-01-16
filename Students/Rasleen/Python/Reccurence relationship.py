# Function 1 
def function1(n):
    if n <= 0:  # Base case: Stop recursion if n is less than or equal to 0
        return
    for i in range(0, n + 1):  # Loop runs (n + 1) times
        print("Codingal")
    function1(n // 2)  # Recursive call with n divided by 2
    function1(n // 3)  # Recursive call with n divided by 3


# Function 2
def function2(n):
    if n <= 1:  # Base case: Stop recursion if n is less than or equal to 1
        return
    print("Codingal")  # Print statement outside base case
    function2(n - 1)  # Recursive call with n decremented by 1


# Calling the functions to get output
print("Output of function1:")
function1(5)  # Example call with n = 5

print("\nOutput of function2:")
function2(5)  # Example call with n = 5