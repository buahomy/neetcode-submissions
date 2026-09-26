# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #copied 
        newNodes =[]
        curr = head
        while curr:
            newNodes.append(curr)
            curr = curr.next

        #spot the toRemove 
        toRemoveIndex = len(newNodes) - n
        if toRemoveIndex == 0: #simply
            return head.next

        #* you can only do .next in linked list as a property
        if toRemoveIndex > 0:
            newNodes[toRemoveIndex - 1].next = newNodes[toRemoveIndex].next            
            return head




