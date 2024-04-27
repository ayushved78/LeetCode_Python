class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        total = 0
        rows=[0]*r
        cols=[0]*c
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    rows[i] += 1
                    cols[j] += 1
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    total += (rows[i]-1)*(cols[j]-1)
        return total