class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        q = deque()
        fresh = 0
        rotten = 0
        minutes = 0
        count=0
        rows = len(grid)
        columns = len(grid[0])
        neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]==2:
                    q.append([i,j])
                    count+=1
                if grid[i][j]==1:
                    fresh+=1
        while len(q)!=0:
            freshFound = False
            iterations = count
            count = 0
            for c in range(iterations): #to check iteration all rotten oranges
                s = q.popleft()
                for index in neighbors:
                    x = index[0]+s[0]
                    y = index[1]+s[1]
                    if (x in range(rows) and y in range(columns)) and grid[x][y]==1:
                        q.append([x,y])
                        grid[x][y]=2
                        rotten +=1
                        count+=1
                        freshFound = True
            if freshFound: #checking if there was any fresh in neighbors
                minutes+=1
        if fresh == rotten:
            return minutes
        return -1