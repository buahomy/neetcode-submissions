class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        if not edges:
            return None
        # union-find
        par = list(range(len(edges) + 1))
        rank = [0] * (len(edges) + 1) 

        # find
        def find(u):
            if par[u] != u:
                par[u] = find(par[u])
            return par[u]    

        # union
        def union(u, v):
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return True

            # union by rank
            if rank[root_u] < rank[root_v]:
                par[root_u] = root_v
            elif rank[root_u] > rank[root_v]:
                par[root_v] = root_u
            else:
                par[root_v] = root_u
                rank[root_u] += 1

            return False        

         # call
        for u, v in edges:
            if union(u, v):
                return [u, v]
        return None       

               
