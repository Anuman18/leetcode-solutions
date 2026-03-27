"""
Problem: Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/
"""

def isPalindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]s