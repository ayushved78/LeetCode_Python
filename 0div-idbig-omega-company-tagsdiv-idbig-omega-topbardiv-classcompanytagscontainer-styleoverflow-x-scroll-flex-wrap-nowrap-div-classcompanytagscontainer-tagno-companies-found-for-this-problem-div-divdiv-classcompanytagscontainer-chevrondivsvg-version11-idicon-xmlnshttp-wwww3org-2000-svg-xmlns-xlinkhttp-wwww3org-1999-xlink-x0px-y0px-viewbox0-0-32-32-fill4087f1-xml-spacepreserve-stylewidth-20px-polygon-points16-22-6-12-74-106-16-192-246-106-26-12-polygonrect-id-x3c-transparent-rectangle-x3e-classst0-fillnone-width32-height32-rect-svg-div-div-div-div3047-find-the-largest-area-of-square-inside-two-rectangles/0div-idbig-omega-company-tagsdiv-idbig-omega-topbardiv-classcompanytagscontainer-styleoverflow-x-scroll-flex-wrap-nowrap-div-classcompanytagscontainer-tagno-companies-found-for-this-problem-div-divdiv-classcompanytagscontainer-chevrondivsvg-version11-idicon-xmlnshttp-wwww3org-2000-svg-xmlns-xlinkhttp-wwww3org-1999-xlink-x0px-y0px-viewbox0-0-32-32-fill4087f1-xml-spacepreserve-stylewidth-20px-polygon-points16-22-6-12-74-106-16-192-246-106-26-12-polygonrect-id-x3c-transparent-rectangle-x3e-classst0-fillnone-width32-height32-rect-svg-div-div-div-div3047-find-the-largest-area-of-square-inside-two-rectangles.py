class Solution:
    def largestSquareArea(self, b: List[List[int]], tr: List[List[int]]) -> int:
        val = 0
        area = 0
        n = len(b)
        for i in range(n):
            for j in range(i+1,n):
                minX = max(b[i][0],b[j][0])
                minY = max(b[i][1],b[j][1])
                maxX = min(tr[i][0],tr[j][0])
                maxY = min(tr[i][1],tr[j][1])
                if maxX > minX and maxY > minY:
                    val = min(maxX-minX,maxY-minY)
                    area = max(val*val, area)
                    
        return area