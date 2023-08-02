class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        start=0
        end=len(matrix)-1
        if end==-1:
            return False
        while(start<=end):
            mid=(start+end)/2
            midRow = matrix[mid]
            if target>midRow[-1]:
                start = mid+1
            elif target<=midRow[-1] and target>=midRow[0]:
                break
            else:
                end=mid-1
        row=mid
        print(row)
        
        start=0
        end=len(matrix[row])-1
        while start<=end:
            mid=(start+end)/2
            if matrix[row][mid]==target:
                break
            if target>matrix[row][mid]:
                start=mid+1
            else:
                end=mid-1
        column=mid
        if matrix[row][column] == target:
            return True
        else:
            return False