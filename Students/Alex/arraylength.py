def recursive_length(lst):
    
    if not lst:
        return 0
    
    else:
        return 1 + recursive_length(lst[1:])


example_list = [1, 2, 3, 4, 5]
print("Length of the list:", recursive_length(example_list))