class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        #base
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]


        #dfs
        def dfs(r, c, prevHeight, ocean):
            if (r < 0 or c < 0 or r >= rows or c >= cols):
                return
            if ((r, c) in ocean or heights[r][c] < prevHeight):
                return
            ocean.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, heights[r][c], ocean)
                
        #travese through both oceans
        for r in range(rows):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, cols - 1, heights[r][cols - 1], atl)

        for c in range(cols):
            dfs(0, c, heights[0][c], pac)
            dfs(rows - 1, c, heights[rows - 1][c], atl) 


        #main
        output = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c)in atl:
                    output.append([r, c])
        return output        
