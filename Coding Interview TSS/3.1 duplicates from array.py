
def remove_duplicates(nums):
    unique_nums = []
    unique_nums.append(nums[0])
    
    n = len(nums)
    for i in range(1, n):
        if nums[i] != nums[i - 1]:
            unique_nums.append(nums[i])
            
    return len(unique_nums)

# Note