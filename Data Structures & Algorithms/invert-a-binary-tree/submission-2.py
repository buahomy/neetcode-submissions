# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # O(n) Space
        stack = [root] #Ex. [1,2,3,4,5,6,7] -> [1]
        while stack:
            # from the top
            node = stack.pop() #[1]
            # *invert the binary children (must be at once)
            node.left, node.right = node.right, node.left
            # next to visit
            if node.left:
                stack.append(node.left)
            if node.right: #so the original left get visited first
                stack.append(node.right)
        return root        