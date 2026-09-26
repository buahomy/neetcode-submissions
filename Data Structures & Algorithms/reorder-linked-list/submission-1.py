# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head:
            return 

        # say Ex. [1, 2, 3, 4, 5]
        newNodes = []    
        cur = head
        while cur:
            newNodes.append(cur)
            cur = cur.next

        i, j = 0, len(newNodes) - 1 
        while i < j and newNodes[i]:
            newNodes[i].next = newNodes[j]
            i += 1 #to split the 2nd half
            
            newNodes[j].next = newNodes[i]
            j -=1

        newNodes[i].next = None  #end the linked list     