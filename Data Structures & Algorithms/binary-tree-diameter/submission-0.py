# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxx = [0]

        def maxDiameter(node):
            if not node:
                return 0
            left = maxDiameter(node.left)
            right = maxDiameter(node.right)

            maxx[0] = max(maxx[0], left + right)
            return 1 + max(left, right)

        maxDiameter(root)
        return maxx[0]        