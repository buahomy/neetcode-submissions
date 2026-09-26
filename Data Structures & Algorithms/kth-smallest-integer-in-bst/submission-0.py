# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        #Stack (DFS)
        # can't do stack = [root], need curr as a placeholder
        stack = []
        curr = root

        while stack or curr: # need *or stack* because at the end of child node
            # deal with the 1st root
            while curr: 
                stack.append(curr) # visit 2nd
                curr = curr.left # 1st
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right # 3rd

