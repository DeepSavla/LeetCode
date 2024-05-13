class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        q = deque()
        minutes = 0
        count=0
        rows = len(grid)
        columns = len(grid[0])
        neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]==2 and (i,j) not in visited:
                    q.append([i,j])
                    count+=1
        while len(q)!=0:
            freshFound = False
            iterations = count
            count = 0
            for c in range(iterations):
                s = q.popleft()
                for index in neighbors:
                    x = index[0]+s[0]
                    y = index[1]+s[1]
                    if (x in range(rows) and y in range(columns)) and (x,y) not in visited and grid[x][y]==1:
                        q.append([x,y])
                        grid[x][y]=2
                        count+=1
                        freshFound = True
                        visited.add((x,y))
            if freshFound:
                minutes+=1
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] ==1:
                    return -1
        return minutes
        
                        
                    