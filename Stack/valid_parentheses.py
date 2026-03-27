"""
Problem: Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/
"""

def isValid(s):
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}

    for c in s:
        if c in mapping:
            if not stack or stack.pop() != mapping[c]:
                return False
        else:
            stack.append(c)

    return not stack