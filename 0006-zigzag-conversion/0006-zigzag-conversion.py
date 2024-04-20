class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        resList = []
        row = 0
        direction = 1
        for i in range(numRows):
            resList.append("") 
        for i in range(len(s)):
            resList[row] += s[i]
            if direction ==-1:
                if row == 0:
                    direction = 1
                    row = row+1
                else:
                    row=row-1
            else:
                if row == numRows-1:
                    direction = -1
                    row = row-1
                else:
                    row = row=row+1
        return "".join(resList)