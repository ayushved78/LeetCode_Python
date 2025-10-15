class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pds = set() # postivie diag movement r+c
        nds = set() # negative diag movement r-c

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r+c) in pds or (r-c) in nds:
                    continue
                
                cols.add(c)
                pds.add(r+c)
                nds.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                cols.remove(c)
                pds.remove(r+c)
                nds.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res