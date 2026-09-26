# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 2 placeholders: one for attaching, the other for returning
        dummy = ListNode() # dummy -> ...
        node = dummy

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next # move the next one after used
            else:
                node.next = list2
                list2 = list2.next # goes the same here
            node = node.next # to the next one after attaching

        # attach remaining nodes if there's any in either (when one is empty)
        if list1:   
            node.next = list1
        else:
            node.next = list2

        return dummy.next # return the one after dummy

        


        # attach the remaining nodes if there's one in either