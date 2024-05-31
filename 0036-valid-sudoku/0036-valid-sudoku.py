class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #one for loop to check row set:
        #one for loop to check column set
        #then check 3x3 smaller squares
        
        boxes = []  #creating nins sets for each boxes
        for i in range(9):  #making 9 empty sets in an array for every 3x3 box; smaller squares are denoted 0-8 index where 0-2 are of first row, 3-5 are second row and 6-8 are third row
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
                curBox = ((i//3)*3) + (j//3)    #calculating box number based on i and j values so proper3x3 box are created
                if board[i][j] in boxes[curBox] and board[i][j]!=".":
                    return False
                boxes[curBox].add(board[i][j])
        return True