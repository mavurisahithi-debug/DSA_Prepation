def max_subarray(nums):
    current = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current = max(nums[i], current + nums[i])
        max_sum = max(max_sum, current)

    return max_sum

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
