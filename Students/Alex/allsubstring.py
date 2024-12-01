def get_substrings(s):
    substrings = []
    length = len(s)
    for i in range(length):
        for j in range(i + 1, length + 1):
            substrings.append(s[i:j])
    return substrings


user_input = input("Enter a string: ")
substrings = get_substrings(user_input)


print("All substrings:")
print(" ".join(substrings))