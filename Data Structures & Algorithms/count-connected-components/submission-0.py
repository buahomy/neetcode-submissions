class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ids = [i for i in range(n)]

        for edge in edges: 
            self.union(edge[0], edge[1], ids)

        #count no. of unique parents and return len()
        parent_set = set()
        for i in range(n):
            parent = self.find(i, ids)
            parent_set.add(parent)

        return len(parent_set)        

    def union(self, edge1: int, edge2:int, ids: List[int]):
        parent1 = self.find(edge1, ids)
        parent2 = self.find(edge2, ids)
        ids[parent1] = parent2 #not dict, replaced

    def find(self, edge: int, ids: List[int]) -> int:
        if ids[edge] != edge:
            ids[edge] = self.find(ids[edge], ids) 

        return ids[edge]    
