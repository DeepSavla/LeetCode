class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        q = deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append([i,j])
        distance = 0
        while q:
            l = len(q)
            distance +=1
            for i in range(l):
                source = q.popleft()
                for d in directions:
                    r = source[0] + d[0]
                    c = source[1] + d[1]
                    if r in range(len(rooms)) and c in range(len(rooms[0])) and distance < rooms[r][c]:
                        q.append([r,c])
                        rooms[r][c] = distance
        return rooms
    
    
        
# Normal:                        
# iterate over matrix
# for every gate: start BFS in 4 directions and update the value of cell if distance from gate is less that the current value of the cell. if cell vualue is updated, add it to the BFS queue
            
#Cannot do DFS here. We want simultaneous spread in all 4 directions. DFS will lead to more distances because the next cell in next column might be called by some other call whose DFS has started.        
                    
#optimal
#Similar to rotten oranges. First add all gates to the queue. Then initiate breadth-first search (BFS) from all gates at the same time.