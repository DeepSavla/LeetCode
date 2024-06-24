class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        ogColour = image[sr][sc]
        dir =[[0,1],[0,-1],[-1,0],[1,0]]
        visited = set()
        q = deque()
        q.append([sr,sc])
        visited.add((sr,sc))
        image[sr][sc] = color
        while q:
            curCell = q.popleft()
            for i in dir:
                curRow = curCell[0]+i[0]
                curCol = curCell[1]+i[1]
                if (curRow in range(rows)) and (curCol in range(cols)) and image[curRow][curCol] == ogColour and (curRow,curCol) not in visited:
                    q.append([curRow,curCol])
                    visited.add((curRow,curCol))
                    image[curRow][curCol] = color
        return image
                    