class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque() 
        #to add all rotten whose neighbors hav not been traversed
        fresh = 0 
        #to keep a count of total fresh initially
        rotten = 0 
        #to track total rotten so that we can compare if all fresh have rotten or not
        minutes = 0
        #to track time to get all rotten
        count=0
        #we only want to perform DFS on oranges that have rotten just previously
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
            if count>0: #checking if there was any fresh in neighbors
                minutes+=1
        if fresh == rotten:
            return minutes
        return -1