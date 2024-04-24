def twoSum(nums, target) -> list:
    for num in nums:
        for num2 in nums:
            if num != num2 and num + num2 == target:
                return [nums.index(num), nums.index(num2)]

print(twoSum([3, 4, 2], 6))