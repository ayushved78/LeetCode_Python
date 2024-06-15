class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        ans = [[] for row in range(numRows)]
        row = 0
        direction = 1
        for it in s:
            ans[row].append(it)
            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1
            row += direction
        for i in range(numRows):
            ans[i] = "".join(ans[i])
        return "".join(ans)