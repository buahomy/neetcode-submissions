# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #Ex. [1,2,3,4,5]
        #finding the middle element by slow and fast points to split into 2 halves
        slow, fast = head, head.next #fast = head.next here so that it splits the second half (less than) properly 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next  
        #otherwise, exit the loop, and this is where it gets the 2nd half -> [4,5]
        second_half = slow.next   
        #break link -> automatically convert the original to the 1st half >> [1,2,3]
        slow.next= None 

        #*start here
        #typical reversing linked list from Ex.1
        prev = None
        while second_half:
            temp = second_half.next #save the next point
            second_half.next = prev  #None
            prev = second_half # prev= cur 
            second_half = temp

        #merge both halves in the given order
        first_half, second_half = head, prev
        while second_half:
            temp1, temp2 = first_half.next, second_half.next #saved (before linked list is changed and newly attached)
            first_half.next = second_half
            second_half.next = temp1;  # attach the 2nd element of first half to 1st element of second half after attaching
            first_half, second_half = temp1, temp2 