nums = [1,2,3,4,5,6,7]
def rotate(nums, k):
    new_nums = []
    for x in range(len(nums)):
        current_index = (x - k) % len(nums)
        new_nums.append(nums[current_index])
    return new_nums

print(rotate(nums, 3))