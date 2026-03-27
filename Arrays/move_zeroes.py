Problem: Move Zeroes
Link: https://leetcode.com/problems/move-zeroes/
Difficulty: Easy

Approach:
- Two pointer
- Swap non-zero forward

Time Complexity: O(n)
Space Complexity: O(1)
"""

def moveZeroes(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1