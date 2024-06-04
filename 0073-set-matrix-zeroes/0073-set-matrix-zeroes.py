class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        targetCells = deque()
        rows=len(matrix)
        columns = len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j]==0:
                    targetCells.append([i,j])
        while len(targetCells)!=0:
            curCell =  targetCells.popleft()
            for i in range(rows):
                for j in range(columns):
                    matrix[i][curCell[1]] = 0
                    matrix[curCell[0]][j] = 0
        
                    
        