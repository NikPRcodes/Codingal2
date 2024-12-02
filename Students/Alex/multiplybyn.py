
def multiply_one_iteration(a, b):
    return a * b


def multiply_n_iterations(a, b):
    result = 0
    for _ in range(b):
        result += a
    return result


a = int(input("Enter 'a' for a*b: "))  
b = int(input("Enter 'b' for a*b: "))  


result_one_iteration = multiply_one_iteration(a, b)
result_n_iterations = multiply_n_iterations(a, b)

print(f"1 iteration: {result_one_iteration}")
print(f"N iteration: {result_n_iterations}")