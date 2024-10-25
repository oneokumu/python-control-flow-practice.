def has_pair_with_sum(nums, target):
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False

# Example usage
nums = [2, 7, 11, 15]
target = 9
print(has_pair_with_sum(nums, target))