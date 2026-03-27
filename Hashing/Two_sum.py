"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
"""

def twoSum(nums, target):
    d = {}
    for i, num in enumerate(nums):
        if target - num in d:
            return [d[target - num], i]
        d[num] = i