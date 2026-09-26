# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # to append & store value in each level
        output = []

        queue = deque()
        queue.append(root)

        while queue:
            
            subOutputLevel = [] #another one to append to output
            for i in range(len(queue)): #by each level
                node = queue.popleft()

                # always check if there is
                if node:
                    subOutputLevel.append(node.val) #retrived in each level

                    #the next to be explored
                    queue.append(node.left) 
                    queue.append(node.right)

            if subOutputLevel:
                output.append(subOutputLevel)  
        return output                  