nums = [2,2,1,1,1,2,2]
def majorityElement(nums):
    value_counts = {}
    for num in nums:
        if num not in value_counts.keys():
            value_counts[num] = 1
        else:
            value_counts[num] += 1
    high_value_index = None
    for key in value_counts.keys():
        if high_value_index is None:
            high_value_index = key
        if value_counts[key] > value_counts[high_value_index]:
            high_value_index = key
    return high_value_index



print(majorityElement(nums))