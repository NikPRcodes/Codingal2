
def find_missing_number(arr):
    n = len(arr) + 1  
    expected_sum = n * (n + 1) // 2  
    actual_sum = sum(arr)  
    missing_number = expected_sum - actual_sum 
    return missing_number


arr = [1, 4, 3, 2, 6]
print(find_missing_number(arr))
