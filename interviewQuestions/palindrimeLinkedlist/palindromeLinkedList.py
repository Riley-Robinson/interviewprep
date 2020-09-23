

#234. Palindrome Linked List
#https://leetcode.com/problems/palindrome-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        values = []
        cur = head
        while cur is not None:
            values append(cur.val)
            cur = cur.next
            
        values_reversed = list(reversed(values))

        return values = values_reversed
        

                    
