class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        firstRowHasZero = False
        firstColHasZero = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] ==0:
                    if i == 0:
                        firstRowHasZero = True
                    if j==0:
                        firstColHasZero = True
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        #do not change the first column from initial values
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j] = 0
        #now changing first row and column
        if firstRowHasZero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if firstColHasZero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
'''
for looop to check matrix
- if any 0:
    - Set that row and column start as zero
Second for loop to set 0
- if 

'''