def find_max_number(numbers):
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number

# According to thye e.g :
nums = (10, 20, 30, 40, 50)
print(find_max_number(nums))
