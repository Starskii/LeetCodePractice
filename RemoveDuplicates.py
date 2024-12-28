nums = [0, 0, 1, 2, 2]

def removeDuplicates(nums):
    unique_count = 1
    write_ptr = 1
    read_ptr = 1
    while write_ptr < len(nums) and read_ptr < len(nums):
        if nums[read_ptr] > nums[read_ptr - 1]:
            unique_count += 1
            nums[write_ptr] = nums[read_ptr]
            write_ptr += 1
        read_ptr += 1
    return unique_count

print(removeDuplicates(nums))