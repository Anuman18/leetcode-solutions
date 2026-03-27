"""
Problem: Sort Array By Parity
Link: https://leetcode.com/problems/sort-array-by-parity/
"""

def sortArrayByParity(nums):
    return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 != 0]