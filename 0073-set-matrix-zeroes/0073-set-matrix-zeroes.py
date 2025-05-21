class Solution:
    def setZeroes(self, g: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r, c = [[*map(all,q)] for q in (g,zip(*g))]
        for i,j in product(range(len(g)),range(len(g[0]))):
            g[i][j] *= r[i]&c[j]