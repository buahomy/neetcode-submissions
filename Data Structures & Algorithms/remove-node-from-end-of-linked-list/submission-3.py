# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # 3rd Approach
        # using N to find len() instead

        N = 0
        curr = head
        while curr:
            N += 1
            curr = curr.next

        toRemoveIndex = N - n
        if toRemoveIndex == 0:
            return head.next

        if toRemoveIndex > 0:
            #get the *prev node to point
            curr = head
            for i in range(toRemoveIndex-1):
                curr = curr.next
        #*skip
        curr.next = curr.next.next
        return head 
               




