class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # DFS
        # Step1
        # above, under, right, left
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        islands = 0

        # Step3 (moved up)
        # Like the previous on in Trie, filter out all the invalid cased and let the recursion
        # Explore all lands connected the cell
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0'):
                # base case — stop recursion or braching(go back to the previous call)
                return

            grid[r][c] = '0' #mark as visited
        
            # *Recursion explore all 4 neighbors
            # dr is “delta row” — how much you move up or down
            # dc is “delta column” — how much you move left or right
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Step2
        # 2D traversal
        for r in range(rows):
            for c in range(cols):
                #* start
                if grid[r][c] == '1': 
                    dfs(r, c)
                    islands += 1

        return islands                

        

                 