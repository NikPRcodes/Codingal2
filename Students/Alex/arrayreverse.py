

def reverseArray(arr):
    
    left, right = 0, len(arr) - 1
    
    
    while left < right:
        
        arr[left], arr[right] = arr[right], arr[left]
        
        
        left += 1
        right -= 1
    
    return arr

arr = [6, 5, 4, 3, 2, 1]
print("Original array:", arr)
reversed_arr = reverseArray(arr)
print("Reversed array:", reversed_arr)
