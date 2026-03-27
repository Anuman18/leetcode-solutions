"""
Problem: Reverse Linked List
Link: https://leetcode.com/problems/reverse-linked-list/
"""

def reverseList(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev