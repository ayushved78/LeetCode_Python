class Solution:
    def islandPerimeter(self, g: List[List[int]]) -> int:
        return sum(g[i][j]*(2-(i>0)*g[i-1][j]-(j>0)*g[i][j-1]) for i,j in product(range(len(g)),range(len(g[0]))))*2
