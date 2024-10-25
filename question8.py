def keys_greater_than_n(d, n):
    result = []
    for key, value in d.items():
        if value > n:
            result.append(key)
    return result

# Example in usage
sample_dict = {'a': 5, 'b': 12, 'c': 3}
n = 4
print(keys_greater_than_n(sample_dict, n))
