# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head) #dummy → 1 → 2 → 3 → ...
        left = dummy 
        right = head

        # say [1, 2, 3, 4, 5], n = 2 
        while n > 0:
            right = right.next
            n -= 1
            # >> [3, 4, 5]

        # DO all this to spot n 
        # because right started n steps ahead
        # when right hits the end None, left will be just before the node to delete.
        while right:
            left = left.next
            right = right.next
        # left would be at [3] when right points to None

        left.next = left.next.next # *skip (it's abstract just know that they're all pointers and do the work)
        return dummy.next #so that can return the lineked list properly here        



