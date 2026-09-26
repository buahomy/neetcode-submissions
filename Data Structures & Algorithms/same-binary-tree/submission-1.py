# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        # Queue
        queue1 = deque([p])
        queue2 = deque([q])

        while queue1 and queue2:
            for i in range(len(queue1)): #BFS rule

                # nodes assigned
                nodeP = queue1.popleft()
                nodeQ = queue2.popleft()

                # 3 comparisons
                if nodeP is None and nodeQ is None:
                    continue
                if nodeP is None or nodeQ is None:
                    return False
                if nodeP.val != nodeQ.val:
                    return False

                # 1 by 1 in BFS order
                queue1.append(nodeP.left) # it'd reach this
                queue1.append(nodeP.right)
                queue2.append(nodeQ.left) # and this first for next loop
                queue2.append(nodeQ.right)

        return True

