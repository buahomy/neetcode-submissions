# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS starting from the bottom building up, this is enough
        if not root: 
            return 0

        # Recursively call
        # O(h) Space, where h is height of tree
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))    
