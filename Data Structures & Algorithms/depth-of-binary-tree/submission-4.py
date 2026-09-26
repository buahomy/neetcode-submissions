# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
    
        def dfs(root):
            if not root:
                return 0
            else:
                leftTree = dfs(root.left)
                rightTree = dfs(root.right)
                maxHeight = 1 + max(leftTree, rightTree)
            return maxHeight
        return dfs(root)



