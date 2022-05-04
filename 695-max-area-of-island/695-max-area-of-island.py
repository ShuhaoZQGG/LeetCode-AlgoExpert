class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    curr = 0
                    stack = [(r, c)]
                    visited.add((r,c))
                    dirs = [[1,0],[0,1],[-1,0],[0,-1]]
                    while stack:
                        r0, c0 = stack.pop()
                        curr += 1
                        for dr, dc in dirs:
                            row = r0 + dr
                            col = c0 + dc
                            if row in range(rows) and col in range(cols) and grid[row][col] == 1 and (row, col) not in visited:
                                stack.append((row,col))
                                visited.add((row,col))
                            res = max(res, curr)
        return res