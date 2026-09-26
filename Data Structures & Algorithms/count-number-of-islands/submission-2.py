class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # BFS (with Queue)
        # Step1
        # above, under, right, left
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        # *The only change (without call stack -> need to generate Queue)
        # Step3 
        def bfs(r, c):
            q = deque()
            grid[r][c] = '0' #marked
            q.append((r, c)) #as a tuple to visit

            while q:
                # *Begin
                row, col = q.popleft()
                for dr, dc in directions:
                    # * It's the same DFS use recursion later to check these
                    # But these are to lay out to check more direct
                    #nc -> new column to explore
                    #nr -> new row to explore
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == '0'):
                        # Move to next iteration BFS
                        continue

                    # It'd come here -> 1st after bfs(r, c is called)
                    q.append((nr, nc)) #visited
                    grid[nr][nc] = '0' #marked

        # Step2
        # 2D traversal
        for r in range(rows):
            for c in range(cols):
                #* start
                if grid[r][c] == '1': 
                    bfs(r, c)
                    islands += 1

        return islands                

        # yay

        

                 