class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        columns = len(matrix[0])
        directions = {0:[0,1],1:[1,0],2:[0,-1],3:[-1,0]}# 0 means right, 1 means down, 2 means left and 3 means top i.e. in order of spirals
        direction = 0
        visited = set()
        cell = [0,0]
        res = [matrix[0][0]]
        visited.add((0,0))
        while(1):
            added = False
            nextRow = cell[0] + directions[direction][0]
            nextColumn = cell[1] + directions[direction][1]
            if nextRow in range(rows) and nextColumn in range(columns) and (nextRow,nextColumn) not in visited:
                visited.add((nextRow,nextColumn))
                res.append(matrix[nextRow][nextColumn])
                cell = [nextRow,nextColumn]
                added = True
            else:
                direction = (direction+1)%4
                nextRow = cell[0] + directions[direction][0]
                nextColumn = cell[1] + directions[direction][1]
                if nextRow in range(rows) and nextColumn in range(columns) and (nextRow,nextColumn) not in visited:
                    visited.add((nextRow,nextColumn))
                    res.append(matrix[nextRow][nextColumn])
                    cell = [nextRow,nextColumn]
                    added = True
            if added == False:
                break
        return res
                
                