class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def BFS(r,c):
            q = deque()
            q.append([r,c])
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            while len(q)!=0:
                curCell = q.popleft()
                for d in directions:
                    row = curCell[0] + d[0]
                    col = curCell[1] + d[1]
                    if (row in range(rows) and col in range(columns)) and (row,col) not in visitedCells and grid[row][col] =='1':
                        q.append([row,col])
                        visitedCells.add((row,col))
        
        #main code
        rows = len(grid)
        columns = len(grid[0])
        visitedCells = set()
        totalIslands = 0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == '1' and (r,c) not in visitedCells:
                    totalIslands+=1
                    visitedCells.add((r,c))
                    BFS(r,c)
        return totalIslands
                    
        
            