def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        comp = target - num
        if comp in num_map:
            return [num_map[comp], i]
        num_map[num] = i
nums = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target: "))
result = two_sum(nums, target)
print("Indices:", result)