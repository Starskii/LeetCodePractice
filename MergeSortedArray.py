nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1


def merge(nums1, m, nums2, n):
    nums1_p = m - 1
    nums2_p = n - 1
    for p in range(m + n - 1, -1, -1):
        if nums2_p > -1 and nums1_p > -1:
            if nums2[nums2_p] > nums1[nums1_p]:
                nums1[p] = nums2[nums2_p]
                nums2_p -= 1
            else:
                nums1[p] = nums1[nums1_p]
                nums1_p -= 1
        elif nums2_p > -1:
            nums1[p] = nums2[nums2_p]
            nums2_p -= 1
        else:
            nums1[p] = nums1[nums1_p]
            nums1_p -= 1
    return nums1

print(merge(nums1, m, nums2, n))