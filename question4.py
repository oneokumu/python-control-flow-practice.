def reverse_strings(strings):
    reversed_list = [s[::-1] for s in strings]
    return reversed_list


input_strings = ["apple", "banana", "cherry"]
print(reverse_strings(input_strings))  # Output: ["elppa", "ananab", "yrrehc"]
