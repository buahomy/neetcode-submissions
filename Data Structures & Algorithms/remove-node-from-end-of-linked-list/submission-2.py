# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #copied into an array
        newNodes =[]
        curr = head
        while curr:
            newNodes.append(curr)
            curr = curr.next

        #spot the toRemove 
        toRemoveIndex = len(newNodes) - n
        if toRemoveIndex == 0: #simply
            return head.next

        #* in a linked list, you can't go backward—you only have .next
        # find the node before X, call it prev.
        # then, make prev.next point to X.next, essentially skipping over X.
        if toRemoveIndex > 0:
            newNodes[toRemoveIndex - 1].next = newNodes[toRemoveIndex].next            
            return head #remember, linked list is handled *in-place




