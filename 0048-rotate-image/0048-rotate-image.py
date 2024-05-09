class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        top = 0
        bottom = len(matrix)-1
        while top<=bottom:
            left = top
            right = bottom
            for i in range(right-left): #coz addition and substraction we want from 0 to number ele in current square row minus 1
                temp = matrix[top][left+i]
                matrix[top][left+i] = matrix[bottom-i][left]
                matrix[bottom-i][left]= matrix[bottom][right-i]
                matrix[bottom][right-i]= matrix[top+i][right]
                matrix[top+i][right] =temp
            top +=1
            bottom-=1 
# for explanation refer https://www.youtube.com/watch?v=fMSJSS7eO1w