class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
#         USING LINEAr SEARCH
        # for i in range(row):
        #     for j in range(col):
        #         if matrix[i][j] == target:
        #             return True
        # return False
        
#         USING BINARY SEARCH
        l = 0
        r = (row * col) - 1
        while l<=r:
            m = (l+r) // 2
            i = m // col
            j = m % col
            
            if target < matrix[i][j]:
                r = m - 1
            elif target > matrix[i][j]:
                l = m + 1
            else:
                return True
        return False