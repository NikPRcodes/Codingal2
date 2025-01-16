def single(a, b):
    return a*b

def n_iterations(a, b):
    result = 0

    for _ in range(abs(b)):
        result += a
        if b < 0:
            result = -result
        return result
    
a = int(input("Enter 'a' for a*b: "))
b = int(input("Enter 'b' for a*b: "))
result_single = single(a, b)
result_n_iterations = n_iterations(a, b)
print("\n1 iteration:", result_single)
print("N iteration:", result_n_iterations)