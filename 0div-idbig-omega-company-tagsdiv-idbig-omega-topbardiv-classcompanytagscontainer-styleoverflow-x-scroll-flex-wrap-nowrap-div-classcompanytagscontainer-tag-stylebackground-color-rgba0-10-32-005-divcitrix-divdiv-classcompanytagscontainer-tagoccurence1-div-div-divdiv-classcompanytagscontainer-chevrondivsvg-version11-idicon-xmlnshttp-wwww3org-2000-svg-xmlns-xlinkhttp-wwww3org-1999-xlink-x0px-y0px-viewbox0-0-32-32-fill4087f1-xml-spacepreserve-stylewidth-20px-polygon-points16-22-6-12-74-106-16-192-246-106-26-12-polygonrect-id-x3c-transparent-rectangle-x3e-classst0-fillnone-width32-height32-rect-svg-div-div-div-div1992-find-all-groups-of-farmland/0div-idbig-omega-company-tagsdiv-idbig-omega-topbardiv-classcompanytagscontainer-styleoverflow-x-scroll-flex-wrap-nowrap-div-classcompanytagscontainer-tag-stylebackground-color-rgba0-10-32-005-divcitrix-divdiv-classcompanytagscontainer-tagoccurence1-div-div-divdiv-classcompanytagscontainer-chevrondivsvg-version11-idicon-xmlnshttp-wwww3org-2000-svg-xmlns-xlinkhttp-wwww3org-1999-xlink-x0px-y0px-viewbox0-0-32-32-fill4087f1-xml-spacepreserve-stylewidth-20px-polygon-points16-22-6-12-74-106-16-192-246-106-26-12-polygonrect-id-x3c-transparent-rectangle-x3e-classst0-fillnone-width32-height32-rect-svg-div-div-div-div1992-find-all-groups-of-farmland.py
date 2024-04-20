class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        # COPIED
        groups = []
        for i in range(0, len(land)):
            for j in range(0, len(land[i])):
                if land[i][j] == 1:
                    group = [i, j]
                    max_x, max_y = [i], [j]
                    
                    self.findFarmlandUtil(land, i, j, max_x, max_y)
                    group.extend([max_x[0], max_y[0]])
                    groups.append(group)
        
        return groups
    
    def findFarmlandUtil(self, land: list[list[int]], i: int, j: int, maxX: list[int], maxY: list[int]):
        land[i][j] = 0

        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for points in range(len(dir)):
            i1 = i + dir[points][0]
            i2 = j + dir[points][1]

            if i1 >= 0 and i2 >= 0 and i1 < len(land) and i2 < len(land[i]):
                if land[i1][i2] == 1:
                    maxX[0] = max(i1, maxX[0])
                    maxY[0] = max(i2, maxY[0])
                    self.findFarmlandUtil(land, i1, i2, maxX, maxY)