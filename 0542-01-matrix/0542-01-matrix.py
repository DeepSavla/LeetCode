class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        q = deque()
        visited = set()
        currentDist = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append([i,j])
                    visited.add((i,j))
        while q:
            curLevelNodes = len(q)
            for i in range(curLevelNodes):
                n = q.popleft()
                curRow = n[0]
                curCol = n[1]
                for d in directions:
                    r = curRow + d[0]
                    c = curCol + d[1]
                    if r in range(rows) and c in range(cols) and (r,c) not in visited:
                        visited.add((r,c))
                        q.append([r,c])
                        if mat[r][c] == 1:
                            mat[r][c] = currentDist + 1
                            
            currentDist +=1
        return mat