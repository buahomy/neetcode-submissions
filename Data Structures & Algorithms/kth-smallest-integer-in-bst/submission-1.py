# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []
        curr = root 

        # need curr for beginning of root node only, the rest would be appended on stack
        while curr or stack:
            # go all the way the the bottom most left first to start dfs on stack [] from there
            while curr:
                stack.append(curr) # [_, ] first on the stack, would be 2nd 
                curr = curr.left # to visit first (will be popped right away)
            curr = stack.pop()
            k -= 1

            if k == 0:
                return curr.val

            curr = curr.right # check right child node before going up  

