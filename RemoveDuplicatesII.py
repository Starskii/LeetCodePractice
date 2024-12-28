nums = [0, 0, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5]

def removeDuplicates(nums):
    write_ptr = 1
    current_unique_count = 1
    while write_ptr < len(nums):
        if nums[write_ptr] != nums[write_ptr - 1]:
            current_unique_count = 1
        else:
            current_unique_count += 1
        if current_unique_count > 2:
            nums.pop(write_ptr)
            write_ptr -= 1
        write_ptr += 1
    return len(nums)

print(removeDuplicates(nums))