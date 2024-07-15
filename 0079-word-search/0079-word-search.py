class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def backtrack(pos,wordIndex,visited):
            if wordIndex == len(word):
                return True
            for d in directions:
                i = pos[0]+d[0]
                j = pos[1]+d[1]
                if (i,j) not in visited and i in range(rows) and j in range(cols) and board[i][j]== word[wordIndex]:
                    visited.add((i,j))
                    if backtrack([i,j],wordIndex+1,visited):
                        return True
                    visited.remove((i,j))
        for r in range(rows):
            for c in range(cols):
                if board[r][c] ==word[0]:
                    if backtrack([r,c],1,{(r,c)}) == True:
                        return True
        return False