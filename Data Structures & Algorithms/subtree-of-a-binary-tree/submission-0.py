# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        #Stack

        # 3 cases of it happening
        if not subRoot: #empty subRoot
            return True
        if not root:
            return False    
        if self.sameTree(root, subRoot): #this is when found the same root nodes at the start
            return True
        # otherwise go check the rest of subRoot either left or right if there's a matach -> if yes subTree is called to thorougly check    
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    #*Helper function to check all nodes of both trees if their roots match
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # 3 cases of comparison again
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val: #if exists, and the nodes match -> check the whole subTree
            #recursively checking all child nodes and verify if -> True
            return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))
     
        return False    

