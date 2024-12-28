nums = [0, 0, 1, 2, 2]

def removeDuplicates(nums):
    unique_count = 0
    write_ptr = 0
    read_ptr = 0
    while write_ptr < len(nums) and read_ptr < len(nums):
        if nums[read_ptr] not in nums[0:write_ptr]:
            unique_count += 1
            nums[write_ptr] = nums[read_ptr]
            write_ptr += 1
            read_ptr += 1
        else:
            read_ptr += 1
    return unique_count

print(removeDuplicates(nums))