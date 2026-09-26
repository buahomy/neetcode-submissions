# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = [0]
        def dfs(root):
            if not root:
                return 0
            else:
                leftTree = dfs(root.left)
                rightTree = dfs(root.right)
                subDiameter = leftTree + rightTree
                diameter[0] = max(subDiameter, diameter[0])
            return 1 + max(leftTree, rightTree)
        dfs(root)
        return diameter[0]