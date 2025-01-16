import numpy as np

# 1. Create an array consisting of linearly spaced elements between 0 to 9
arr = np.arange(10)
print("Original Array:", arr)

# 2. Replace all odd numbers in this array with -1 without modifying the original array
arr_copy = arr.copy()  
arr_copy[arr_copy % 2 != 0] = -1
print("Array with odd numbers replaced by -1:", arr_copy)

# 3. Create a new array that contains the original 1-dimensional array converted into a 2-dimensional array with two rows
arr_2d = arr.reshape(2, -1)
print("2D Array (2 rows):")
print(arr_2d)

# 4. Iterate through the original array and find out the sum of all even numbers
even_sum = np.sum(arr[arr % 2 == 0]) 
print("Sum of all even numbers in the original array:", even_sum)