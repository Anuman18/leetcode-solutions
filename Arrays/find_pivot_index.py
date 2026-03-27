
Problem: Find Pivot Index
Link: https://leetcode.com/problems/find-pivot-index/
"""

def pivotIndex(nums):
    total = sum(nums)
    left = 0
    for i in range(len(nums)):
        if left == total - left - nums[i]:
            return i
        left += nums[i]
    return -1