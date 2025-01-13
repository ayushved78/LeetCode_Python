from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        pairs = 0
        n = len(grid)
        rows = defaultdict(int)
        for row in grid:
            rows[tuple(row)] += 1
        for c in range(n):
            column = tuple(grid[r][c] for r in range(n))
            if column in rows:
                pairs += rows[column]
        return pairs