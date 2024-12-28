nums = [3, 2, 2, 3]
val = 3


def removeElement(nums, val):
    for x in range(len(nums)):
        if nums[x] == val:
            for y in range(len(nums) - 1, x, -1):
                if nums[y] != val:
                    nums[x] = nums[y]
                    nums[y] = val
                    break
    k = 0
    for x in nums:
        if x != val:
            k += 1
    return k

print(removeElement(nums, val))