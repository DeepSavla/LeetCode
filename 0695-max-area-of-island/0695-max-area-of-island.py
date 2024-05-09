class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visitedCell = set()
        q = deque()
        area = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]] 
        # find all 1 in matrix that are not visited and perform BFS in its 4 directions
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                curArea = 0
                if grid[i][j] == 1 and (i,j) not in visitedCell:
                    q.append([i,j])
                    visitedCell.add((i,j))
                    while len(q)!=0:
                        s = q.popleft()
                        curArea +=1
                        for d in directions:
                            x = s[0]+d[0]
                            y = s[1]+d[1]
                            if (x in range(len(grid)) and y in range(len(grid[0]))) and (x,y) not in visitedCell and grid[x][y] == 1: #understand conditions
                                q.append([x,y])
                                visitedCell.add((x,y))
                    area = max(area,curArea)
        return area
                        
                    