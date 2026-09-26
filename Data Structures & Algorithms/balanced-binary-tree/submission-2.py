# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        balanced = [True]
        def dfs(root):
            if not root:
                return 0
            leftTree = dfs(root.left)
            rightTree = dfs(root.right)
            diff = abs(leftTree - rightTree)
            if diff > 1:
                balanced[0] = False            
            return 1 + max(leftTree, rightTree)
        
        dfs(root)
        return balanced[0]