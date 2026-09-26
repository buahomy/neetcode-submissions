# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        # Stack (DFS)
        output = []

        # starter pack
        stack = [(root, 0)] 
        while stack:
            node, level = stack.pop()

        
            if len(output) == level: #this is smart (having the len in [...] and match with level)
                output.append([])

            # yay done
            output[level].append(node.val) 

            # DFS 
            # Push right first so left gets processed first (L-to-R)
            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))

        return output


        

        