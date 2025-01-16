def sort_array(arr):
    low = 0  
    mid = 0  
    high = len(arr) - 1 
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]  # Swap 0 to its correct position
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1  # 1 is already in the correct position
        else:
            arr[high], arr[mid] = arr[mid], arr[high]  # Swap 2 to its correct position
            high -= 1

    return arr

# Example usage:
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 10]
arr = [x for x in arr if x in {0, 1, 2}]  # Remove any elements other than 0, 1, or 2
sorted_arr = sort_array(arr)
print(" ".join(map(str, sorted_arr)))