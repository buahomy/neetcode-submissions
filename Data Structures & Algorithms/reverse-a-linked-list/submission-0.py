# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next #must save original next here because the linked list is reversed in O(1) space
            curr.next = prev #the linked list in now changed
            prev = curr
            curr = temp
        return prev    
        