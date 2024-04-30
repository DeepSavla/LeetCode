class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def BFS(cell):
            q = deque()
            q.append(cell)
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            while len(q)!=0:
                curCell = q.popleft()
                for d in directions:
                    nwR = curCell[0] + d[0]
                    nwC = curCell[1] + d[1]
                    if (nwR in range(rows) and nwC in range(columns)) and (nwR,nwC) not in visitedCells and grid[nwR][nwC] =='1':
                        q.append([nwR,nwC])
                        visitedCells.add((nwR,nwC))
        
        rows = len(grid)
        columns = len(grid[0])
        visitedCells = set()
        totalIslands = 0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == '1' and (r,c) not in visitedCells:
                    totalIslands+=1
                    visitedCells.add((r,c))
                    BFS([r,c])
        return totalIslands
                    
        
            