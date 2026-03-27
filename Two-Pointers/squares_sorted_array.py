"""
Problem: Squares of Sorted Array
Link: https://leetcode.com/problems/squares-of-a-sorted-array/
"""

def sortedSquares(nums):
    return sorted([x*x for x in nums])