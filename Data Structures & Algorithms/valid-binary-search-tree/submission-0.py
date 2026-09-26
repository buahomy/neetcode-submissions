# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # 3-element tuple
        queue = deque([(root, float("-inf"), float("inf"))]) #starter pack, just initial bound placeholder, no rea

        while queue:
            node, left, right = queue.popleft()
            if not (left < node.val < right):
                return False

            #then typical BFS for child nodes (keep in mind -> node, left, right)
            if node.left:
                queue.append((node.left, left, node.val))
            if node.right:
                queue.append((node.right, node.val, right))   

        return True         

        