# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #pointers slow(move one step) and fast(move two steps)
        slow, fast = head, head

        # check if there's a node to point to, if cycle exists (*infinite pointing) it'd enter this loop
        # otherwise, it'd point to 'None' and exit the loop
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            #fast would eventually lap (no matter how big or where it loops) to slow
            if fast == slow:
                return True
        return False        