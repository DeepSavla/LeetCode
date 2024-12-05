class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        numberOfIslands = 0
        neighbours = [[0,1],[0,-1],[1,0],[-1,0]]
        
        def DFS(i,j):
            for n in neighbours:
                row = i+n[0]
                col = j+n[1]
                if (row,col) not in visited and row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] =="1":
                    visited.add((row,col))
                    DFS(row,col)
                
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j]=="1":
                    numberOfIslands +=1
                    visited.add((i,j))
                    DFS(i,j)
                    
        return numberOfIslands