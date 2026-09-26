# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        q = deque([root])

        while q:
            right = None

            # BFS (level-order)
            qLevel = len(q)
            for i in range(qLevel):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    right = node

            if right:
                output.append(right.val)
        return output      