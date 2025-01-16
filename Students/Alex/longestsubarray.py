def longest_alternating_subarray(arr):
    if not arr:
        return 0
    
    
    max_length = 1  
    current_length = 1
    
    for i in range(1, len(arr)):
        
        if (arr[i] % 2 == 0 and arr[i - 1] % 2 != 0) or (arr[i] % 2 != 0 and arr[i - 1] % 2 == 0):
            
            current_length += 1
        else:
            
            current_length = 1
        
        
        max_length = max(max_length, current_length)
    
    return max_length


arr = [6, 4, 9, 4, 7, 2, 3, 4, 2, 52]
result = longest_alternating_subarray(arr)
print(result)