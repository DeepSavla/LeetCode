class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #one for loop to check row set:
        #one for loop to check column set
        #then check 3x3 squares
        boxes = []  #creating nins sets for each boxes
        for i in range(9):
            boxes.append(set())
        for i in range(9):
            rowEle = set()
            columnEle = set()
            for j in range(9):
                if board[i][j]!= ".":   #checking all rows for same element
                    if board[i][j] in rowEle:
                        return False
                    rowEle.add(board[i][j])
                if board[j][i]!= ".":   #Checking all columns for same element
                    if board[j][i] in columnEle:
                        return False
                    columnEle.add(board[j][i])
                curBox = ((i//3)*3) + (j//3)
                if board[i][j] in boxes[curBox] and board[i][j]!=".":
                    return False
                boxes[curBox].add(board[i][j])
        return True