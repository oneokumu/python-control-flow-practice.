def tuples_to_dict(tuples_list):
    result_dict = {}
    for key, value in tuples_list:
        result_dict[key] = value
    return result_dict

# Example in usage
sample_list = [("apple", 20), ("banana", 5)]
print(tuples_to_dict(sample_list))
