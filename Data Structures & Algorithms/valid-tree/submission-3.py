class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1):
            return False

        # edges -> adj list
        adj = defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        # DFS (cycle detection & traversal for connectedness)
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False  

            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent: # undirected, so gotta make sure
                    continue
                if not dfs(neighbor, node): #traversal recurisvely inside
                    return False
            return True

        return dfs(0, -1) and len(visited) == n
        