def largest(arr):
    max_val = arr[0]

    for num in arr:
        if num > max_val:
            max_val = num

    return max_val

print(largest([10, 20, 4, 45, 99]))
