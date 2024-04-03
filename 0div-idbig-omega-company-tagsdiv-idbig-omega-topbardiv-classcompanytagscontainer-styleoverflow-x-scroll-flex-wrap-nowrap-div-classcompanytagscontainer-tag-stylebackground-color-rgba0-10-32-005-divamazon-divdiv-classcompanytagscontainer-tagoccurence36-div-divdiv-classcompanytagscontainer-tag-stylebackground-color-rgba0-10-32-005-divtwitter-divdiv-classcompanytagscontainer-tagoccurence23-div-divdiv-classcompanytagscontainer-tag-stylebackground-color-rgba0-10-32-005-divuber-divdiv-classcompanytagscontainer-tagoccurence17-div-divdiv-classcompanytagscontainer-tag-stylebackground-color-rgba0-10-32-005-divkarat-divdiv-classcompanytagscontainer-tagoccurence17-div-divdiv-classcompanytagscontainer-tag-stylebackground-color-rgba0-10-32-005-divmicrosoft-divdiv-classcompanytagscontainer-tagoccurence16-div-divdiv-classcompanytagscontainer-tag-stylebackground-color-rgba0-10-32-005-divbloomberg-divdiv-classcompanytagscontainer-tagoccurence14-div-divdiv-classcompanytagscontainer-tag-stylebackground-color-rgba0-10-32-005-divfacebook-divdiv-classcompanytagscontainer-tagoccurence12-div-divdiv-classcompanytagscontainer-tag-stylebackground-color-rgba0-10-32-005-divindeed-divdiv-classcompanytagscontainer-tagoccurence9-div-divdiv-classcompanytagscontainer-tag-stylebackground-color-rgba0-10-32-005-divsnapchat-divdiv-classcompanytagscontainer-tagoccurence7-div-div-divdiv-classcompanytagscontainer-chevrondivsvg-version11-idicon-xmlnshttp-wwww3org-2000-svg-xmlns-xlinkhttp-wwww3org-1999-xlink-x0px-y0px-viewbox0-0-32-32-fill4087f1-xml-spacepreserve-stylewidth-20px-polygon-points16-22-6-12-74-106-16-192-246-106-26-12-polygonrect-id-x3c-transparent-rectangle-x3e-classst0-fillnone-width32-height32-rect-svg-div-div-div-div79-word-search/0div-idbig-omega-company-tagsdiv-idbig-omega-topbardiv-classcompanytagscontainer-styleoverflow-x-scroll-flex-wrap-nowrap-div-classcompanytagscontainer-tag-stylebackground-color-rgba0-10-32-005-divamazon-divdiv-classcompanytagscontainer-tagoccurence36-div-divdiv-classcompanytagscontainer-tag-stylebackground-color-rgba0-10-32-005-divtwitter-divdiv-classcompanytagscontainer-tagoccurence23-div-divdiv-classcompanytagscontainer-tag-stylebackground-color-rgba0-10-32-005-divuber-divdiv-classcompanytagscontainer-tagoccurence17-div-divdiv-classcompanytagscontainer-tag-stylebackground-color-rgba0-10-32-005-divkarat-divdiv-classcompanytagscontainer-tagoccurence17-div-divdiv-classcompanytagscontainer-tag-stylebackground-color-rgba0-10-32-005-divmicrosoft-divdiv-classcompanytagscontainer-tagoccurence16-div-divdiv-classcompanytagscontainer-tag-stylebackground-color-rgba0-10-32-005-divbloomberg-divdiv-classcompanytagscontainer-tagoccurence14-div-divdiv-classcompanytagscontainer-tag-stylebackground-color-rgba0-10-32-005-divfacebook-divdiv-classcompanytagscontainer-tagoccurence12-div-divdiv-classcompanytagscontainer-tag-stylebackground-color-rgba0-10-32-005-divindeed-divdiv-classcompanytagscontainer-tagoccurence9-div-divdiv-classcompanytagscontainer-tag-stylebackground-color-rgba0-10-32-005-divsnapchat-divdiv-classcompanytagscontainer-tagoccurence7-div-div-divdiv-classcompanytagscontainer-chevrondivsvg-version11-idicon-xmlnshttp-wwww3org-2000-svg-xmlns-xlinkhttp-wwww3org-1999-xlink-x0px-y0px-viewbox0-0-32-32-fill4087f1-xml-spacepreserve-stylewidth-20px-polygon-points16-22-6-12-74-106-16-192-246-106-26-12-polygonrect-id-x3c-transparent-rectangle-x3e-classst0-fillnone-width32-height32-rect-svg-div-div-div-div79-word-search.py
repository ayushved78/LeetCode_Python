class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        p = len(word)
        
        def helper(r,c,pos):
            # check if the position is nearby lenght of word
            if pos >= p:
                return True
            # check the r,c, and pos of word
            elif 0<=r<m and 0<=c<n and board[r][c] == word[pos]:
                # backtracking
                temp = board[r][c]
                board[r][c] = None
                # movement in forward, backward, updard and downward direction
                if helper(r+1,c,pos+1) or helper(r-1,c,pos+1) or helper(r,c+1,pos+1) or helper(r,c-1,pos+1):
                    return True
                board[r][c] = temp
            
            return False
        
        # iterations in the words
        for r in range(m):
            for c in range(n):
                if helper(r,c,0):
                    return True
        
        return False