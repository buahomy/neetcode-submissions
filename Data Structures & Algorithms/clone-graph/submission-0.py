"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        #Return -> A new Node object with .neighbors list that matches the structure


        # DFS (ofc preferred in Graph Traversal Pattern1)
        # with Hash Map (Dict) >> map original nodes -> copied version
        # Hash -> each node is copied once only
        oldToNew = {}

        def dfs(node):
            # To catch after dfs(neighbor) is called
            # Avoid same node(in cyclic) or shared node((e.g., two nodes both point to the same third node))
            if node in oldToNew:
                return oldToNew[node]

            #*Start here
            copy = Node(node.val)
            oldToNew[node] = copy #key copied
            for neighbor in node.neighbors:
                # *1-> get the clone of that neighbor with dfs(neighbor)  
                # 2-> then copied(or appended) to neighbors property of copy
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node) if node else None    

