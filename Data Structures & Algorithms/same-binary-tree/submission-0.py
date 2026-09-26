# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        root1, root2 = p, q
        # DFS through stack
        
        # (root1, root2) as tuples
        stack = [(p, q)]
        while stack:
            root1, root2 = stack.pop()
            #if root1 != root2: *objects can be called like this 
                #return False
            # *use .val and None instead (3 cases of checking False)
            if not root1 and not root2:
                continue
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False        

            stack.append((root1.left, root2.left))
            stack.append((root1.right, root2.right))
        return True        
