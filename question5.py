def print_even_keys(d):
    for key, value in d.items():
        if value % 2 == 0:
            print(key)

# Example in usage
sample_dict = {'a': 2, 'b': 3, 'c': 4}
print_even_keys(sample_dict)  #  The Output is : 'a' 'c'
