class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        for i in range(rows):
            for j in range(cols):
                liveNeighbourCell = 0
                for d in directions:
                    r = i + d[0]
                    c = j + d[1]
                    if r in range(rows) and c in range(cols) and (board[r][c]== 1 or board[r][c]== -1):
                        liveNeighbourCell +=1
                print(liveNeighbourCell)
                if liveNeighbourCell < 2 and board[i][j]==1:
                    board[i][j] = -1    # for live that have died
                elif liveNeighbourCell > 3 and board[i][j]==1:
                    board[i][j] = -1    # for live that have died
                elif liveNeighbourCell == 3 and board[i][j]==0:
                    board[i][j] = 2     # for died that can now live
        for i in range(rows):
            for j in range(cols):
                if board[i][j]<=0:
                    board[i][j] = 0
                else:
                    board[i][j] = 1
        