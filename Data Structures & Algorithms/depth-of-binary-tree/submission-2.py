# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # DFS through stack
        # (node, level) as tuples
        stack = [(root, 1)]
        max_level = 0

        while stack:
            node, level = stack.pop()
            # traversing down
            if node:
                max_level = max(max_level, level)
                # children node
                stack.append((node.left, level + 1))
                stack.append((node.right, level + 1))
        return max_level        

