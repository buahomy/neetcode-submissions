class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        countFresh = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    countFresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        if countFresh == 0:
            return 0

        time = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        countFresh -= 1
                        q.append((nr, nc))
            time += 1
        
        if countFresh == 0:
            return time - 1
        else:
            return -1